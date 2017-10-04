
## 例

app/sitempaps.py:

~~~py
# coding: utf-8
from django.contrib.sitemaps import Sitemap
from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from myarticles.models import Article


class AppSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Article.objects.all()


def sitemap_urls():
    sitemaps = {
        'main': AppSitemap(),
    }
    return [
        url('^sitemap.xml', sitemap, {'sitemaps': sitemaps}),
        url('^sitemap-(?P<section>.+).xml', sitemap, {'sitemaps': sitemaps}),
    ]
~~~    


app/urls.py:

~~~py
from django.conf.urls import url, include
from django.contrib import admin
from app import sitemaps

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    ....
] + sitemaps.sitemap_urls()
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
