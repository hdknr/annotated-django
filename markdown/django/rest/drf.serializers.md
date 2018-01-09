##  ContentType シリアライザ

配信:

- `content_object` のシリアライザを `content_type` で判定する(`resolve_serializer()`)
- このシリアライザで `SerializerMethodField` で配信する

受信:

- `is_valid` の際に、 `initial_data` から `content_type` を抜く
- `content_type` データのシリアライザを同様に `content_type` で判定する
- このシリアライザで、データを保存し、保存されたオブジェクトの `id` を `object_id` に上書き更新する

~~~py
class Gadget(models.Model):
    name = models.CharField(verbose_name=_('Gadget Name'), max_length=50)
    category = models.ForeignKey( Category, null=True, blank=True, default=None)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
~~~

~~~py
class GadgetSerializer(serializers.ModelSerializer):
    content_type = ContentTypeField()         # app_lable + "_" + model
    content_object = serializers.SerializerMethodField()

    def get_content_object(self, obj):
        ser = self.resolve_serializer(self.key(obj))
        return ser(obj.content_object).data

    class Meta:
        model = models.Gadget
        fields = '__all__'

    @classmethod
    def resolve_serializer(cls, key):
        return {
            'mymedia_mediafile': MediaFileSerializer,
            'mymedia_album': AlbumSerializer,
            'mywords_word': WordSerializer,
        }.get(key, None)

    def key(self, instance):
        return '_'.join(instance.content_type.natural_key())

    def is_valid(self, raise_exception=False):
        self.patch_content_object()
        return super(GadgetSerializer, self).is_valid(
            raise_exception=raise_exception)

    def patch_content_object(self):
        content_object = self.initial_data.pop('content_object', {})
        ser = self.resolve_serializer(self.initial_data['content_type'])
        ser = ser and ser(data=content_object)
        obj = ser and ser.is_valid() and ser.save()
        if obj:
            self.initial_data['object_id'] = obj.id
~~~

## 外部キーで参照する複合インスタンスを(idではなく)キーで指定する

- Selectionモデルが Usageモデル を　外部キーで参照
- Usage は `slug` がユニークキー

JSON:

~~~js
{
  ....
  usage: {slug: 'catch'}
}
~~~

~~~py

class SelectionSerializer(serializers.ModelSerializer, OrderableMixin):
    usage = UsageSerializer(required=False)

    class Meta:
        model = models.Selection
        fields = '__all__'
~~~        

~~~py
class UsageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Usage
        fields = '__all__'

    def run_validation(self, data=fields.empty):
        # slug が指定されていたら検索検索する
        usage = ('slug' in data) \
            and models.Usage.objects.filter(slug=data['slug']).first()
        # みつからなかったら、スーパークラスに処理させる(新規でUsageが作られる)
        return usage \
            or super(UsageSerializer, self).run_validation(data=data)
~~~
