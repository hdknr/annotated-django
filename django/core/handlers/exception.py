import logging
import sys
from functools import wraps

from django.conf import settings
from django.core import signals
from django.core.exceptions import (
    PermissionDenied, RequestDataTooBig, SuspiciousOperation,
    TooManyFieldsSent,
)
from django.http import Http404
from django.http.multipartparser import MultiPartParserError
from django.urls import get_resolver, get_urlconf
from django.views import debug

logger = logging.getLogger('django.request')


def convert_exception_to_response(get_response):
    """
    django.core.handlers.baseげget_responseを例外処理する
    正常時には get_response() の戻りをそのまま返す.
    例外が発生したらエラー応答に変えて返答する。


    Wrap the given get_response callable in exception-to-response conversion.

    All exceptions will be converted. All known 4xx exceptions (Http404,
    PermissionDenied, MultiPartParserError, SuspiciousOperation) will be
    converted to the appropriate response, and all other exceptions will be
    converted to 500 responses.

    This decorator is automatically applied to all middleware to ensure that
    no middleware leaks an exception and that the next middleware in the stack
    can rely on getting a response instead of an exception.
    """
    @wraps(get_response)
    def inner(request):
        try:
            response = get_response(request)
        except Exception as exc:
            response = response_for_exception(request, exc)
        return response
    return inner


def response_for_exception(request, exc):
    # エラー発生時の応答
    if isinstance(exc, Http404):
        if settings.DEBUG:
            response = debug.technical_404_response(request, exc)
        else:
            # 404 の記録と例外応答
            response = get_exception_response(request, get_resolver(get_urlconf()), 404, exc)

    elif isinstance(exc, PermissionDenied):
        logger.warning(
            'Forbidden (Permission denied): %s', request.path,
            extra={'status_code': 403, 'request': request},
        )
        # 403 の記録と例外応答
        response = get_exception_response(request, get_resolver(get_urlconf()), 403, exc)

    elif isinstance(exc, MultiPartParserError):
        logger.warning(
            'Bad request (Unable to parse request body): %s', request.path,
            extra={'status_code': 400, 'request': request},
        )
        # 404 の記録と例外応答
        response = get_exception_response(request, get_resolver(get_urlconf()), 400, exc)

    elif isinstance(exc, SuspiciousOperation):
        if isinstance(exc, (RequestDataTooBig, TooManyFieldsSent)):
            # POST data can't be accessed again, otherwise the original
            # exception would be raised.
            request._mark_post_parse_error()

        # The request logger receives events for any problematic request
        # The security logger receives events for all SuspiciousOperations
        security_logger = logging.getLogger('django.security.%s' % exc.__class__.__name__)
        security_logger.error(
            str(exc),
            extra={'status_code': 400, 'request': request},
        )
        if settings.DEBUG:
            response = debug.technical_500_response(request, *sys.exc_info(), status_code=400)
        else:
            # 400 の記録と応答
            response = get_exception_response(request, get_resolver(get_urlconf()), 400, exc)

    elif isinstance(exc, SystemExit):
        # Allow sys.exit() to actually exit. See tickets #1023 and #4701
        raise

    else:
        signals.got_request_exception.send(sender=None, request=request)
        # 500 の記録と応答 
        response = handle_uncaught_exception(request, get_resolver(get_urlconf()), sys.exc_info())

    # Force a TemplateResponse to be rendered.
    if not getattr(response, 'is_rendered', True) and callable(getattr(response, 'render', None)):
        response = response.render()

    return response


def get_exception_response(request, resolver, status_code, exception, sender=None):
    # エラーコードに対する例外応答を生成して返す
    # handle_uncaught_exceptionで loggingする 
    try:
        callback, param_dict = resolver.resolve_error_handler(status_code)
        response = callback(request, **dict(param_dict, exception=exception))
    except Exception:
        signals.got_request_exception.send(sender=sender, request=request)
        # 500エラーの記録と応答
        response = handle_uncaught_exception(request, resolver, sys.exc_info())

    return response


def handle_uncaught_exception(request, resolver, exc_info):
    """
    500エラー: 例外の報告: 
    logger.errror(
        'message...', 
        exc_info=sys.exc_info,
        extra={'status_code': 500, 'request': request}
    )
    # https://docs.python.org/3.6/library/sys.html#sys.exc_info

    Processing for any otherwise uncaught exceptions (those that will
    generate HTTP 500 responses).
    """
    if settings.DEBUG_PROPAGATE_EXCEPTIONS:
        raise

    logger.error(
        'Internal Server Error: %s', request.path,
        exc_info=exc_info,
        extra={'status_code': 500, 'request': request},
    )

    if settings.DEBUG:
        return debug.technical_500_response(request, *exc_info)

    # Return an HttpResponse that displays a friendly error message.
    callback, param_dict = resolver.resolve_error_handler(500)
    return callback(request, **param_dict)
