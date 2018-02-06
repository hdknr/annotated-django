## DRF(Django REST Framework) での Implict Flowでのトークン受け取り

### サーバー

viewsets.py:

~~~py
from rest_framework import (viewsets, response)
from social_django.utils import load_strategy, load_backend
from social_django.views import _do_login


class TokenViewSet(viewsets.ViewSet):

    def auth(self, request):
        backend_name = request.data.get('backend', 'oauth2')
        backend = load_backend(load_strategy(request), backend_name, '')
        user = user if request.user.is_authenticated else None
        res = backend.do_auth(
            request.data.get('access_token', ''),
            response=request.data, user=user, request=request)
        _do_login(backend, res, getattr(res, 'social_user', None))
        return res

    def create(self, request):
        user = self.auth(request)
        return response.Response(dict(username=user and user.username))
~~~

api.py:

~~~py
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()
router.register(r'token', viewsets.TokenViewSet, base_name='token')


urlpatterns = [
    url(r'^', include(router.urls)),
]
~~~

urls.py:

~~~py
from django.conf.urls import url, include
from . import api

urlpatterns = [
    url(r'^api/', include(api)),
]
~~~

### クライアントスクリプト


~~~js
function onAuthorized(response){
  axios.defaults.xsrfCookieName = 'csrftoken';
  axios.defaults.xsrfHeaderName = 'X-CSRFToken';
  response['backend'] = 'amazon';     // Login with Amazon(LwA) (OAuth2)
  axios.post("{% url 'token-list' %}", response).then((res)=>{
      // データ処理 && 画面遷移
  });
}
~~~
