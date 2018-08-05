- https://django-robots.readthedocs.io/en/latest/
- https://github.com/jazzband/django-robots


## 設置


app/urls.py:

~~~py

urlpatterns = [
  ...
  url(r'^robots\.txt', include('robots.urls')),
  ...
]
~~~

app/settings.py:

~~~py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,     #  django.template.loaders.app_directories.Loader
        ...
    },
]

INSTALLED_APPS += [
    'django.contrib.sites',
    'django.contrib.sitemaps',
    ...
    'robots',
    ...
]
SITE_ID = 1
~~~

migrate:

~~~bash
$ python manage.py migrate
~~~


## リソース

- [Robots Database:robotstxt.org](http://www.robotstxt.org/db.html)
- [robots.txt ファイルを作成する](https://support.google.com/webmasters/answer/6062596?hl=ja)
