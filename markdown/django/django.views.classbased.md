Django :Yet Another Class-Based View


- URLConf をビューのメソッドベースでつくる
- メソッドには、 url(正規表現), order(URLConf中の順番)を属性に加える
- これをデコレータでやる
- ビュークラスにはモデルをバインドさせて、nameを生成する


## ベースクラス :View

~~~py
from django.conf import urls
from operator import itemgetter
from django.utils.decorators import method_decorator as _M


class View(object):

    @classmethod
    def handler(cls, url='', name='', order=0, decorators=None):
        '''ビュー処理のでコレータを返します'''
        # その他のデコレータ
        decorators = decorators or [lambda x: x]

        def _handler(func):

            @wraps(func)
            def wrapper(*args, **kwargs):
                # 最初の引数はクラスオブジェクトのはず
                response = func(*args, **kwargs)
                return response

            wrapper.url = url       # URLパターン
            wrapper.name = name     # URL名
            wrapper.order = order   # urlpatternでの順列

            return classmethod(
                reduce(lambda x, y: _M(y)(x), [wrapper] + decorators))

        return _handler

    @classmethod
    def urls(cls):
        ''' urlpatterの配列を返す '''
        def _viewname(func_name):
            if not hasattr(cls, 'Meta'):
                return "_".join([
                    cls.__module__.split('.')[0],
                    cls.__name__.lower(), func_name])
            return "{}_{}_{}".format(
                cls.Meta.models._meta.app_label,
                cls.Meta.models._meta.model_name,
                func_name)

        funcs = []
        for name in cls.__dict__:
            obj = getattr(cls, name)
            if hasattr(obj, 'url'):
                viewname = obj.name or _viewname(name)
                funcs.append((viewname, obj.order, obj))

        # obj.order でソートします
        return [
            urls.url(func.url, func, name=name)
            for name, _, func in sorted(funcs, key=itemgetter(1))
        ]

~~~

## 実際のビュークラス: CommunityView

~~~py
from django.contrib.auth import decorators as authdeco


class CommunityView(View):
    class Meta:
        # バインドするモデル
        models = models.Community

    @handler(
      url=r'^community/(?P<id>.+)/edit(?:/(?P<command>.*))?',
      name='communities_community_edit',
      order=0,
      decorators=[authdeco.permission_required('communities.list_community')])
    def edit(cls, request, id, command=''):
        # .....
        return TemplateResponse(
            request,
            'communities/community/edit{0}.html'.format(name),
            dict(request=request, form=form))

    @handler(
      url=r'^community/(?P<id>.+)',
      name='communities_community_detail',
      order=1,
      decorators=[authdeco.permission_required('communities.list_community')])
    def detail(cls, request, id, *args, **kwargs):
        # .....
        return TemplateResponse(
            request,
            'communities/community/detail.html',
            dict(request=request, instance=instance, form=form))

    @handler(
      url=r'^community',
      name='communities_community_index',
      order=2,
      decorators=[authdeco.permission_required('communities.list_community')])
    @permission_required
    def index(cls, request):
        # ...
        return TemplateResponse(
            request,
            'communities/community/index.html',
            dict(request=request, instances=instances))
~~~

## urls.py


~~~
from django.conf.urls import url    
from . import views

urlpatterns = [        
  # その他のURLConf
  # ....
] + views.CommunityView.urls()
~~~

## 確認

~~~py
In [4]: for url in CommunityView.urls():
   ...:     print url
   ...:     
<RegexURLPattern communities_community_edit ^community/(?P<id>.+)/edit(?:/(?P<command>.*))?>
<RegexURLPattern communities_community_detail ^community/(?P<id>.+)>
<RegexURLPattern communities_community_index ^community>
~~~
