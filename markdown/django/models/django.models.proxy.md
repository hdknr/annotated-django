# プロキシモデル

## 例) 親子関係があるモデル

models.py:

~~~py
from django.db import models
from .import defs, querysets

class Package(defs.Package):

    parent = models.ForeignKey(
        'self', related_name='subpackages', 
        null=True, blank=True, default=None,
        on_delete=models.SET_NULL)


class RootPackage(Package):
    '''トップレベルパッケージ'''
    # Package を継承

    class Meta:
        proxy = True        # 実態は定義されないプロキシモデル

    class Man(models.Manager):
        def get_queryset(self):
            # プロキシモデルとしてフィルターされる条件
            return querysets.PackageQuerySet(
                self.model, using=self._db).toplevels()

    objects = Man()         # マネージャ
~~~

querysets.py:

~~~py
from django.db import models


class PackageQuerySet(models.QuerySet):

    def toplevels(self, **kwargs):
        return self.filter(parent__isnull=True, **kwargs)
~~~

## 記事

- [How to use Django's Proxy Models](http://benlopatin.com/using-django-proxy-models/)
