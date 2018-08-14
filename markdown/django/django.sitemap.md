# Django Sitemap フレームワーク

## 例

app/sitempaps.py:

~~~py
from django.contrib.sitemaps import Sitemap, views
from django.urls import path, re_path


class AppSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        from histories.models import Note
        return Note.objects.all()


sitemaps = {
    'main': AppSitemap(),
}


urlpatterns = [
    path('sitemap.xml', views.sitemap, {'sitemaps': sitemaps}),
    re_path('^sitemap-(?P<section>.+).xml', views.sitemap, {'sitemaps': sitemaps}),
]
~~~    


app/urls.py:

~~~py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path('', include('app.sitemap')),
]
~~~

app/settings.py:

~~~py
INSTALLED_APPS += [
    'django.contrib.sites',
    'django.contrib.sitemaps',
    ....
]
SITE_ID = 1
~~~


## 確認

~~~bash 
$ curl http://localhost:9900/sitemap.xml |  xmllint --format --encode utf-8 - | head -n 10
~~~

~~~xml
<?xml version="1.0" encoding="utf-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>http://example.com/49</loc>
    <changefreq>weekly</changefreq>
    <priority>0.5</priority>
  </url>
  <url>
    <loc>http://example.com/48</loc>
    <changefreq>weekly</changefreq>
~~~


## ping_google

- [ping_google command](https://docs.djangoproject.com/ja/2.1/ref/contrib/sitemaps/#pinging-google)

~~~bash 
$ python manage.py help ping_google
usage: manage.py ping_google [-h] [--version] [-v {0,1,2,3}]
                             [--settings SETTINGS] [--pythonpath PYTHONPATH]
                             [--traceback] [--no-color]
                             [sitemap_url]

Ping Google with an updated sitemap, pass optional url of sitemap

positional arguments:
  sitemap_url

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -v {0,1,2,3}, --verbosity {0,1,2,3}
                        Verbosity level; 0=minimal output, 1=normal output,
                        2=verbose output, 3=very verbose output
  --settings SETTINGS   The Python path to a settings module, e.g.
                        "myproject.settings.main". If this isn't provided, the
                        DJANGO_SETTINGS_MODULE environment variable will be
                        used.
  --pythonpath PYTHONPATH
                        A directory to add to the Python path, e.g.
                        "/home/djangoprojects/myproject".
  --traceback           Raise on CommandError exceptions
  --no-color            Don't colorize the command output.
~~~

例:

~~~bash 
$ python manage.py ping_google [/sitemap.xml]
~~

- sitemmap.xml の受け取りサイズに注意
- Google にURLが登録されていないと `django.contrib.sitemaps.SitemapNotFound` 例外がおきます


## サイトマップ配信ビュー

- [サイトマップビュー · hdknr/annotated-django@85c096d](https://github.com/hdknr/annotated-django/commit/85c096d288392af693a1af5d4437c291570dfa4d)
