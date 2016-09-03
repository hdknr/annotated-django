- [django-oscar/django-oscar](https://github.com/django-oscar/django-oscar/)
- [RTD](https://django-oscar.readthedocs.io/en/releases-1.2/)
- [Django Oscar (ECパッケージ) 日本利用ガイド](http://qiita.com/ytyng/items/a4ae77df8bc4c5506d19)

## Install

django 1.8


[django-compressor](https://django-compressor.readthedocs.io/en/latest/)

-  [rjsmin - JS minifier](https://pypi.python.org/pypi/rjsmin)
-  [django-appconf - A helper class for handling configuration defaults](https://pypi.python.org/pypi/django-appconf/1.0.2)

~~~bash
$ pip install django_compressor
...
Successfully installed
django-appconf-1.0.2 django-compressor-2.1 rcssmin-1.0.6 rjsmin-1.0.12
~~~

django-oscar:

- [Django Extra View - class based views](https://django-extra-views.readthedocs.io/en/latest/)
- [django-haystack - modular search](https://django-haystack.readthedocs.io/en/v2.5.0/)
- [django-tables2 - HTML tables](https://django-tables2.readthedocs.io/en/latest/)
- [django-treebeard - efficient tree](https://tabo.pe/projects/django-treebeard/docs/2.0/)
- [django-widget-tweaks](https://github.com/kmike/django-widget-tweaks)
- [factory-boy](https://factoryboy.readthedocs.io/en/latest/)
- [fake-factory](https://github.com/joke2k/faker)
- [funcsigs - PEP 362/inspect module](http://funcsigs.readthedocs.io/en/0.4/)
- [ipaddress - Python 3.3+'s ipaddress for Python 2.6, 2.7, 3.2](https://github.com/phihag/ipaddress)
- [pbr - setuptools](https://pypi.python.org/pypi/pbr9)
- [phonenumbers - Google's libphonenumber library ](https://github.com/daviddrysdale/python-phonenumbers)
- [pillow - PIL fork](https://github.com/python-pillow/Pillow)
- [purl - URL manipulation](https://github.com/codeinthehole/purl)
- [python-dateutil](https://dateutil.readthedocs.io/en/stable/)
- [pytz](http://pythonhosted.org/pytz/)
- [six](http://pythonhosted.org/six/)
- [sorl-thumbnail](https://sorl-thumbnail.readthedocs.io/en/latest/)

~~~bash
$ pip install django-oscar

...
Successfully installed
Babel-2.3.4 Unidecode-0.4.19
django-1.8.14 django-extra-views-0.6.4 django-haystack-2.4.1 django-oscar-1.2.2
django-tables2-1.0.7 django-treebeard-4.0.1 django-widget-tweaks-1.4.1
factory-boy-2.6.1 fake-factory-0.6.0 funcsigs-1.0.2 ipaddress-1.0.16 mock-1.3.0
pbr-1.10.0 phonenumbers-7.5.1 pillow-3.3.0 purl-1.3
python-dateutil-2.5.3 pytz-2016.6.1 six-1.10.0 sorl-thumbnail-12.3
~~~

[pysolr]

~~~bash
$ pip install pysolr
...
Successfully installed pysolr-3.5.0 requests-2.11.0

$ sudo apt-get isntall solr-jetty
$ sudo /etc/init.d/jetty8 start
~~~

- Django の通常のプロジェクト

~~~bash
$ mkdir web; django-admin startproject app web; cd web
~~~

## 設定

app/oscars.py

~~~py
from oscar.defaults import *            # NOQA
from oscar import get_core_apps
from oscar import OSCAR_MAIN_TEMPLATE_DIR


OSC_TEMPLATES_DIR = [OSCAR_MAIN_TEMPLATE_DIR]

OSC_TEMPLATES_CONTEXT_PROCESSORS = [
    'oscar.apps.search.context_processors.search_form',
    'oscar.apps.promotions.context_processors.promotions',
    'oscar.apps.checkout.context_processors.checkout',
    'oscar.apps.customer.notifications.context_processors.notifications',
    'oscar.core.context_processors.metadata',
]
OSC_APPS = ['compressor', 'widget_tweaks', ] + get_core_apps()
OSC_MIDDLEWARE_CLASSES = (
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)
OSC_AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

OSC_HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr',
        'INCLUDE_SPELLING': True,
    },
}
~~~

app/settings.py

~~~py
...
INSTALLED_APPS = (                                                                  
    ....
    'django.contrib.sessions',                                                      
    'django.contrib.sites',                 # Oscar                                 
    ...
    'django.contrib.flatpages',             # Oscar                                 
)           
...
DATABASES = {                                                                    
    'default': {                                                                 
        'ENGINE': 'django.db.backends.sqlite3',                                  
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),                            
        'ATOMIC_REQUESTS': True,                                                 
    }                                                                            
}    
...
LANGUAGE_CODE = 'ja'                                                             
TIME_ZONE = 'Asia/Tokyo'                                                         
SITE_ID = 1                                                                      
STATIC_ROOT = os.path.join(BASE_DIR, 'static')                                   
MEDIA_URL = '/media/'                                                            
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')                                     

import traceback                                                                 
try:                                                                             
    from app.oscars import *            # NOQA                                   
    TEMPLATES[0]['DIRS'] = [os.path.join(BASE_DIR, 'templates'),] + OSC_TEMPLATES_DIR # NOQA
    TEMPLATES[0]['OPTIONS']['context_processors'] += OSC_TEMPLATES_CONTEXT_PROCESSORS  # NOQA
    INSTALLED_APPS += tuple(OSC_APPS)                                            
    MIDDLEWARE_CLASSES += OSC_MIDDLEWARE_CLASSES                                 
    AUTHENTICATION_BACKENDS = OSC_AUTHENTICATION_BACKENDS                        
    HAYSTACK_CONNECTIONS = OSC_HAYSTACK_CONNECTIONS                              
except:                                                                          
    pass                 
~~~

urls.py

~~~py
from django.conf.urls import include, url                                           
from django.contrib import admin                                                    
from oscar.app import application                                                   


urlpatterns = [                                                                     
    url(r'^i18n/', include('django.conf.urls.i18n')),                               
    url(r'^admin/', include(admin.site.urls)),                                      
    url(r'', include(application.urls)),                                            
]                           
~~~

- 起動

~~~bash
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver 0.0.0.0:8000
~~~

## 日本

- pycountry

~~~bash
$ pip install pycountry
$ python manage.py oscar_populate_countries
Successfully added 249 countries.
~~~

- 日本のみシッピング

~~~bash
$ echo "UPDATE address_country SET is_shipping_country = 0 WHERE printable_name != 'Japan';" | python manage.py dbshell
~~~

### 翻訳

[Translating Oscar within your project](https://django-oscar.readthedocs.io/en/releases-0.5/howto/how_do_i_translate_oscar.html#translating-oscar-within-your-project)

## 拡張

拡張:

- モデル拡張
- ビュー拡張

- モデルフォーク

~~~bash
$ python manage.py oscar_fork_app catalogue oscar_fork

Creating package oscar_fork/catalogue
Creating admin.py
Creating app config
Creating models.py
Creating migrations folder

The final step is to add 'oscar_fork.catalogue' to INSTALLED_APPS
(replacing the equivalent Oscar app). This can be achieved using
Oscars get_core_apps function - e.g.:

  # settings.py
  ...
  INSTALLED_APPS = [
      'django.contrib.auth',
      ...
  ]
  from oscar import get_core_apps
  INSTALLED_APPS = INSTALLED_APPS + get_core_apps(
      ['oscar_fork.catalogue'])
~~~

- app/oscars.py

~~~py
OSC_APPS = ['compressor', 'widget_tweaks', ] + get_core_apps(['oscar_fork.catalogue'])  # NOQA
~~~

## 検索

- Haystack インターフェース
- Haystack 経由で elasticsearch も使えると思う


## pytest

- [pytest-django](https://pytest-django.readthedocs.io/en/latest/tutorial.html)
