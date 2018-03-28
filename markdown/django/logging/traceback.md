## traceback レポートの通知

### LogHandler: Tracebackレポート

- DEBUG=Trueの時にブラウザに返すHTMLをファイルに書き込みます

~~~py
from django.utils import timezone
from django.views.debug import ExceptionReporter
from logging import Handler


def save_to_media(name, content):
    from django.core.files.base import ContentFile
    from django.core.files.storage import FileSystemStorage
    storage = FileSystemStorage()
    return storage.save(filename, ContentFile(content))


class LogHandler(Handler, object):

    def emit(self, record):
        request = getattr(record, 'request', None)
        exc_info = record.exc_info or (None, record.getMessage(), None)
        reporter = ExceptionReporter(request, is_email=False, *exc_info)

        try:
            self.report(request, reporter)
        except:
            # TODO: report エラーをsyslogなどにだす
            pass

    def report(self, request, reporter):
        '''実際のレポート処理'''

        # ファイル名
        day = timezone.now().strftime('%Y-%m-%d')
        filename = 'exception/{}.error.html'.format(day)

        # MEDIA_ROOT 以下にトレースバックのHTMLを書き込む
        save_to_media(filename, reporter.get_traceback_html())
~~~

### ロギング設定

- ERROR が起きた時のハンドラをLogHandlerに処理させます

~~~py
....
EXCEPTION_LOGGER_HANDLER = {
    'level': 'ERROR',
    'class': 'logger.handlers.LogHandler',
}
....
def logging(logdir=None):
    ...
    return dict(
        version=1,
        disable_existing_loggers=False,         # gunicorn.access.log enable
        handlers=dict(
            ....,
            logger=EXCEPTION_LOGGER_HANDLER,
        ),
        loggers=dict(
            django=dict(handlers=['console', 'logger'], level='ERROR'),
        )
    )
~~~

settings.py:

~~~py
try:
    from . import loggings
    LOGGING = loggings.logging(
        os.path.join(os.path.dirname(BASE_DIR), 'logs'))
except:
    pass
~~~    


### 通知


通知スクリプト:

~~~py
#!/home/ubuntu/.anyenv/envs/pyenv/versions/app/bin/python3
# Slackに設定した Webhook URL をコピー
URL = 'https://hooks.slack.com/services/xxxxxxxx/yyyyyyyyyyyyyyy/zzzzzzzzzz'
#
import requests
import sys

if sys.argv[1].endswith('.html'):
    a = f"https://your.service.com/logger/exception/{sys.argv[1]}"
    data = {'text': a}
    print(requests.post(URL, json=data))
~~~

通知設定:

- [incron](https://github.com/hdknr/scriptogr.am/blob/master/command/inotifywait.md#incron) でファイルを検知して Slackに通知する

~~~bash
$ incrontab -l

/path/to/your/app/web/media/exception IN_CREATE /path/to/you/app/bin/exception.py $#
~~~

### 通知ビュー

- 管理者だけが見れるようにする

~~~py
from django.http import HttpResponse
from mimetypes import guess_type
from django.core.files.storage import FileSystemStorage
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def exception(request, path):
    path = 'exception/' + path
    ct, _ = guess_type(path)
    return HttpResponse(
        FileSystemStorage().open(path), content_type=ct)
~~~
