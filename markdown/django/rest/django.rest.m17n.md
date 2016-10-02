DRF: シリアライズデータの国際化(m17n)

- [DRF](http://www.django-rest-framework.org/)

## やりたいこと

- 既存システムが日本語だけ対応
- 端末からの言語指定で言語に応じたデータを返したい
- APIが多いので、メタデータ/インターフェースを変更したくない

## 方針

- Langugeでサポート言語を管理する
- 既存モデル(Line[運行路線]とか)に対してLanguageごとの翻訳データモデル(LineTransとか)を定義する
- ビューの処理開始時にリクエストごとに言語を設定する
- 必要なモデルをシリアライザに渡す
- シリアライザの中で現在の言語の翻訳データがあればモデルのフィールドを書き換える
- シリアライズの結果を以前と同じメタデータで返す

## Language

~~~py
class Language(BaseModel):
    code = models.CharField(u'言語コード')
    label = models.CharField(u'言語ラベル')
~~~  

## 既存モデルのフィールドを翻訳データで書き換えて返す

~~~py
from django.utils import translation

class TransQuerySet(BaseQuerySet):
    def for_lang(self, obj, lang=None):
        lang = lang or translation.get_language()   # 現在の言語
        m17n = self.filter(original=obj, lang__code=lang).first() # 翻訳データ
        if not m17n:
            # 言語の翻訳がなかったらそのまま返す
            return obj
        for field in self.model._meta.fields:   # 置き換える
            name = field.name
            if field.name not in ['original', 'lang']:
                setattr(obj, name, getattr(m17n, name))
        # DO NOT SAVE THIS OBJ
        return obj
~~~  

## 元モデルの翻訳データモデルを定義

- `original` : 元モデル(Lineとか)
- `lang`: Language
- 翻訳が必要なデータは`field_names` で渡す

~~~py
def i18n(cls, *field_names):
    ''' cls: 元となるモデルクラス
        field_names: 翻訳が必要なフィールド
    '''
    def __unicode__(self):
        # 最初のフィールドが表示されるとする
        return unicode(getattr(self, field_names[0], ''))

    meta = type(
        b'Meta', (object, ),
        dict(
            verbose_name="{} {}".format(
                cls._meta.verbose_name,  _('Translation')),
            verbose_name_plural="{} {}".format(
                cls._meta.verbose_name_plural, _('Translation')),
            unique_together=(('original', 'lang',),),  # 言語ごとに１つだけ
        )
    )

    # 元モデルからフィールド名に対応するフィールドクラスをコピーする
    fields = dict(
        (name, cls._meta.get_field(name).clone()) for name in field_names)

    fields['__module__'] = cls.__module__
    fields['Meta'] = meta
    fields['original'] = models.ForeignKey(
        cls, verbose_name=cls._meta.verbose_name, related_name='trans')
    fields['lang'] = models.ForeignKey(
        Language, verbose_name=_('Language'))
    fields['__unicode__'] = __unicode__
    fields['objects'] = querysets.TransQuerySet.as_manager()
    return type(cls._meta.object_name + b"Trans", (models.Model,), fields)
~~~

## 既存モデルの多国語化

~~~py
class Line(models.Model):
  name = models.CharField(u'路線名')
  description = models.TextField(u'路線詳細)
  ... # その他のフィールド
~~~

- `name`  と `description` の翻訳データが必要

~~~py
LineTrans = m17n_models.i18n(Line, 'name', 'description', )
~~~

## Admin

- Line の編集の時に各言語の LineTrans を編集する

~~~py
class LineTransAdminInline(admin.StackedInline):
    model = models.LineTrans
    extra = 0


class LineAdmin(admin.OSMGeoAdmin):
    inlines = [LineTransAdminInline, ]
    ....
~~~


## API

- 指定したエリアでサービスされている路線情報を返す

~~~py
from django.utils import translation

@decorators.api_view(['POST', 'GET'])
@decorators.authentication_classes((authentication.TokenAuthentication,))
@decorators.permission_classes((permissions.IsAuthenticated,))
@permission_required('tourists.change_tourist')
def api_line_list(request, id):
    profile = request.user.profile              # ユーザーのProfile モデル
    translation.activate(profile.language.code) # ユーザーごとの言語設定

    area = Area.objects.get(id=id)
    data = serializers.LineSerializer(area.line_set.all(), many=True).data
    res = JSONResponse(data)
    return res

~~~

## シリアライザ　

- 多言語対応シリアライザをサブクラス
- メタデータは多言語化する前と同じ

~~~py
class LineSerializer(LangModelSerializer):

  class Meta:
      model = models.Line
      exclude = ('enabled', 'created_at', 'updated_at', )
~~~

## 多言語対応シリアライザ


~~~py
from rest_framework import serializers
from collections import OrderedDict


class LangModelSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        '''シリアライズデータを作る'''

        # 翻訳データのリレーションがあったら現在の言語で置き換えたインスタンスにする
        if hasattr(instance, 'trans'):
            instance = instance.trans.for_lang(instance)

        ret = OrderedDict()
        fields = [field for field in self.fields.values()
                  if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except:
                continue

            if attribute is not None:
                represenation = field.to_representation(attribute)
                if represenation is None:
                    # Do not seralize empty objects
                    continue
                if isinstance(represenation, list) and not represenation:
                    # Do not serialize empty lists
                    continue
                ret[field.field_name] = represenation

        return ret
~~~
