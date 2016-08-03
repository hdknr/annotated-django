# 記事

- [Logging](http://docs.python-guide.org/en/latest/writing/logging/)
- [PYTHON: WRITING CUSTOM LOG HANDLER AND FORMATTER](http://masnun.com/2015/11/04/python-writing-custom-log-handler-and-formatter.html)
- [How to write custom python logging handler?](http://stackoverflow.com/questions/3118059/how-to-write-custom-python-logging-handler)

# traceback


- [Print a stack trace to stdout on errors in Django while using manage.py runserver](http://stackoverflow.com/questions/5886275/print-a-stack-trace-to-stdout-on-errors-in-django-while-using-manage-py-runserve)
- [Logging uncaught exceptions in Python](http://stackoverflow.com/questions/6234405/logging-uncaught-exceptions-in-python)


# Django

- [Error reporting](https://docs.djangoproject.com/ja/1.9/howto/error-reporting/)
- [Where in django is the default 500 traceback rendered so that I can use it to create my own logs?](http://stackoverflow.com/questions/12924746/where-in-django-is-the-default-500-traceback-rendered-so-that-i-can-use-it-to-cr)
- [DEFAULT_LOGGING](https://github.com/django/django/blob/1.8/django%2Futils%2Flog.py#L23)
- [django.utils.log.AdminEmailHandler](https://github.com/django/django/blob/1.8/django%2Futils%2Flog.py#L89)

- [BaseHandler で500エラーが起きた時に logger.errorで記録される](https://github.com/hdknr/annotated-django/commit/b8da3eb7d7acda42b945dc3b8f6ea37151bb7978)

# Sentry

- [Logging](https://docs.getsentry.com/hosted/clients/python/integrations/logging/)


~~~py
LOGGING = {
    'disable_existing_loggers': True,

    'handlers': {
        'console': { 'level': 'DEBUG', 'class': 'logging.StreamHandler', },
        'sentry': {
            'level': 'ERROR', 'class': 'raven.handlers.logging.SentryHandler',
            'dsn': 'https://<key>:<secret>@app.getsentry.com/<project>',
            },
        },
    'loggers': {
        '': { 'handlers': ['console', 'sentry'], 'level': 'DEBUG', 'propagate': False, },
    }
}
~~~

- [SentryHandler](https://github.com/getsentry/raven-python/blob/master/raven/handlers/logging.py#L29)
- python [logging.Handler](https://hg.python.org/cpython/file/2.7/Lib/logging/__init__.py#l656)
- [python LogRecord](http://docs.python.jp/3/library/logging.html#logrecord-objects)

- [_log](https://hg.python.org/cpython/file/2.7/Lib/logging/__init__.py#l1267) メソッドでレベル指定で記録する
- 実際は、 [makeRecord](https://hg.python.org/cpython/file/2.7/Lib/logging/__init__.py#l1254)が呼ばれる
- ここで、LogRecordにパラメータがセットされる。
- `extra`(dict) も `record.key = value` でセットされます

# Slack


- [slackpy.SlackLogger](https://github.com/iktakahiro/slackpy/blob/master/slackpy/slackpy.py)
- [Send production errors to slack instead of email](http://stackoverflow.com/questions/29914390/send-production-errors-to-slack-instead-of-email)
