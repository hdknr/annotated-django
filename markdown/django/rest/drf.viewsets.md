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
