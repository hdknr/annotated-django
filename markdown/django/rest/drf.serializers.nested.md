# ネストしたシリアライザの書き込み

## Foreign Key オブジェクトのネスト

- [Writable nested representations](https://www.django-rest-framework.org/api-guide/serializers/#writable-nested-representations)

~~~py
class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status

class IssueSerializer(serializers.ModelSerializer):
    status = StatusSerializer()         #  Issue.statusをネスト

    class Meta:
        model = Issue

    def update(self, instance, validated_data):
        '''更新の場合'''
        status = validated_data.pop('status')
        instance.status_id = status.id
        # その他の処理
        return instance
~~~

## 自己参照モデルのネスト

- [Django rest framework nested self-referential objects - Stack Overflow](https://stackoverflow.com/questions/13376894/django-rest-framework-nested-self-referential-objects)

~~~py
class PackageProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PackageProduct
        fields = '__all__'

    def get_fields(self):
        fields = super().get_fields()
        fields['alternatives'] = PackageProductSerializer(many=True)
        return fields
~~~


## "この項目はnullにできません。"

- `allow_null=True` を設定する

~~~py

class PetSerializer(serializers.ModelSerializer):
    ...
    breed_father = BreedSerializer(required=False, allow_null=True)
    breed_mother = BreedSerializer(required=False, allow_null=True)
~~~

## 記事

- [Django Rest Framework - Updating a foreign key - Stack Overflow](https://stackoverflow.com/questions/33077256/django-rest-framework-updating-a-foreign-key)