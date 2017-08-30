## settings.STATIC_URL

デフォルト:

~~~py
STATIC_URL = '/static/'
~~~


## settings.STATIC_ROOT

~~~py
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(DATA_DIR, 'static')
~~~
