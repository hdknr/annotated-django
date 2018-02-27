## 同じクラスのインスタンスをまとめて生成する

`request.data` のタイプが `list` であれば、 シリアライザを返す時に `many=True` で生成する

~~~py
class AssociateTopicViewSet(viewsets.ModelViewSet):
    .....

    def get_serializer(self, *args, **kwargs):
        '''ModelViewSetの get_serializerをオーバーライドする'''

        serializer_class = self.get_serializer_class()
        context = self.get_serializer_context()
        kwargs['context'] = context

        # many=True の判定
        data = ('request' in context) and getattr(context['request'], 'data', None)
        if isinstance(data, list):
            kwargs['many'] = True
            return serializer_class(*args, **kwargs)

        return serializer_class(*args, **kwargs)
~~~        


## データがSHIFT_JISで送られてくる

- `request.encoding` が設定されていれば、すでにSHIFT_JIS -> UTF-8変換が終わっている
- `request.encoding` == 'None' であれば、QueryDictで再度 `request.body` を `encoding` 指定で変換する

~~~py
from django.http import HttpResponse, QueryDict
from rest_framework import viewsets


class MessageViewSet(viewsets.ViewSet):

    def create(self, request):

        # Shift_JIS(cp932,....)
        data = request.data if request.encoding else \
            QueryDict(request.body, encoding='shift_jis')

        serializer = serializers.MessageSerializer(data=data)
        return serializer.is_valid() and serializer.save()
~~~        
