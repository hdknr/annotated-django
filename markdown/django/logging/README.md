[#46](https://github.com/hdknr/annotated-django/issues/46)


## Django での LOGGING の扱い

- [django.utils.log](https://docs.djangoproject.com/ja/2.0/_modules/django/utils/log/): デフォルトロギング

`django/__init__.py` [setup()](https://github.com/hdknr/annotated-django/commit/e59cdf3ac8a6113e517b51c8c01fcb8a33826842): 

~~~py
def setup(set_prefix=True):
    """
    Configure the settings (this happens as a side effect of accessing the
    first setting), configure logging and populate the app registry.
    Set the thread-local urlresolvers script prefix if `set_prefix` is True.
    """
    from django.apps import apps
    from django.conf import settings
    from django.urls import set_script_prefix
    from django.utils.log import configure_logging

    configure_logging(settings.LOGGING_CONFIG, settings.LOGGING)
    # 関数： settings.LOGGING_CONFIG: logging.config.dictConfig
    # https://docs.python.jp/3/library/logging.config.html#logging.config.dictConfig
    # LOGGING設定情報がLOGGING_CONFIGの関数で初期化される、ということ

    if set_prefix:
        set_script_prefix(
            '/' if settings.FORCE_SCRIPT_NAME is None else settings.FORCE_SCRIPT_NAME
        )
    apps.populate(settings.INSTALLED_APPS)
~~~

- [ロギングデフォルトの設定をおこなってから必要であればカスタム設定](https://github.com/hdknr/annotated-django/commit/5d7692a7e9a70c49a94c3382ef43ad4cdc31d31b)

### extra

- [debug](https://docs.python.jp/3/library/logging.html#logging.debug)
- [LogRecord](https://docs.python.jp/3/library/logging.html#logrecord-objects) オブジェクトに属性が追加される:

~~~py 
from logging import getLogger
getLogger().info('message...', extra={'a': 'hoge', 'b': Exception('OMG!')})
~~~

## フォーマット

- [ltsv](ltsv.md)

## HTTP

- [エラー応答](errors.md)

## トレースバック

- [例外記録と通知](traceback.md)

## gunicorn

- [gunicorn.access.log が記録されない](django.logging.md)
- [gunicorn.log ローテーション](django.logging.md)
