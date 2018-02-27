## "この項目はnullにできません。"

- `allow_null=True` を設定する

~~~py

class PetSerializer(serializers.ModelSerializer):
    ...
    breed_father = BreedSerializer(required=False, allow_null=True)
    breed_mother = BreedSerializer(required=False, allow_null=True)
~~~    
