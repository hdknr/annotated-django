# サンプル

## sample1

~~~py
class TopicSelectionsField(serializers.Field):

    def to_representation(self, obj):
        return obj

    def to_internal_value(self, data):

        def _patch(i):
            i['usage'] = models.Usage.objects.filter(slug=i['slug']).first()
            return i

        return filter(_patch, data)

    def update_selections(self, selections):
        for i in selections:
            self.root.instance.select_for(i['usage'], i['selected'])
~~~

~~~py
class PageSerializer(serializers.ModelSerializer):
    selections = TopicSelectionsField()

    class Meta:
        model = models.Page
        fields = '__all__'

    def save(self, **kwargs):
        selections = self.validated_data.pop('selections', [])
        super(PageSerializer, self).save(**kwargs)
        self.fields['selections'].update_selections(selections)
~~~