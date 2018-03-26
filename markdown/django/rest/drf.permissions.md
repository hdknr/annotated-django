## オブジェクトレベル

- [Object level permissions](http://www.django-rest-framework.org/api-guide/permissions/#object-level-permissions)

### パーミッションクラスでの実装

rest_framework.permissions.BasePermission:

~~~py
class BasePermission(object):

    def has_permission(self, request, view):
        # ビューレベル
        return True   # True: OK,  False: パーミッションなし

    def has_object_permission(self, request, view, obj):
        # オブジェクトレベル
        return True   # True: OK,  False: パーミッションなし
~~~


### ビュー/ビューセットでの実装


rest_framework.views.APIView:

~~~py
class APIView(View):
    ....
    def check_object_permissions(self, request, obj):
        # オブジェクトレベルで確認
        for permission in self.get_permissions():
            if not permission.has_object_permission(request, self, obj):
                self.permission_denied(
                    request, message=getattr(permission, 'message', None)
                )
    ....
~~~    


rest_framework.views.APIView:

~~~py
class GenericAPIView(views.APIView):
    ...

    def get_object(self):
        # クエリセットの取得
        queryset = self.filter_queryset(self.get_queryset())

        # フィルタリングパラメータ
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}

        # クエリ
        obj = get_object_or_404(queryset, **filter_kwargs)

        # オブジェクトレベルのパーミッション
        self.check_object_permissions(self.request, obj)

        return obj
~~~        


## 例

app.perms:

~~~py
from django.contrib.auth import get_permission_codename
from django.contrib.auth.models import Permission


def perm_code(action, model):
    return get_permission_codename(action, model._meta)


def perm_name(action, model):
    return "{}.{}".format(
        model._meta.app_label, perm_code(action, model))
~~~

viewsets:

~~~py
from django.contrib.auth import get_permission_codename
from rest_framework import (permissions, viewsets)
from . import models, serializers, filters
from app.perms import perm_name


class ShopPermission(permissions.IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, obj):
        has_perm = getattr(obj, 'has_perm', lambda user, perm: False)
        return has_perm(request.user, perm_name('change', obj))


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer
    filter_class = filters.OrderItemFilter
    permission_classes = (ShopPermission, )
~~~


models:

~~~py
class Order(models.Model):

    def has_perm(self, user, perm):
        return self.user == user

class OrderItem(models.Model):
    ....
    def has_perm(self, user, perm):
        return self.order.has_perm(user, perm)
~~~
