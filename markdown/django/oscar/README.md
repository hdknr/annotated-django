- [django-oscar/django-oscar](https://github.com/django-oscar/django-oscar/)
- [RTD](https://django-oscar.readthedocs.io/en/releases-1.2/)
- [Django Oscar (ECパッケージ) 日本利用ガイド](http://qiita.com/ytyng/items/a4ae77df8bc4c5506d19)

## Install

- django 1.8

~~~bash
$ pip install django_compressor
...
Successfully installed
django-appconf-1.0.2 django-compressor-2.1 rcssmin-1.0.6 rjsmin-1.0.12

~~~
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



## 検索

- Haystack インターフェース
- Haystack 経由で elasticsearch も使えると思う
