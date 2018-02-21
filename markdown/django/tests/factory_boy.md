- http://factoryboy.readthedocs.io/en/latest/

## Recipe

### レコードをランダムに取得

~~~py
class RandomInstance(factory.LazyFunction):

    def __init__(self, model_class, *args, **kwargs):
        choices = range(model_class.objects.count())
        super(RandomInstance, self).__init__(
            function=lambda: model_class.objects.all()[random.choice(choices)],
            *args, **kwargs
        )
~~~
~~~py

class ApplicationFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.Application

    ...
    shop = RandomInstance(models.Shop)
    ...
~~~


### 関連するフィールドのデータ


~~~py
class ContractorFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.Contractor

    class Params:
        address = RandomInstance(JpAddress)     # 住所テーブルよりランダムなレコードを取得

    ...
    zipcode = factory.LazyAttribute(lambda o: o.address.zipcode)
    prefecture = factory.LazyAttribute(lambda o: o.address.pref_name)
    city = factory.LazyAttribute(lambda o: o.address.city_name)
    town = factory.LazyAttribute(lambda o: o.address.town_name)
    ...
~~~

## 記事

- [Djangoでfactory_boyを使ってテストをする１](http://qiita.com/hys/items/90a9f1af90e10a8cd4e1)
- [Djangoでfactory_boyを使ってテストをする２](http://qiita.com/hys/items/19a03aaac87a93e0d539#_reference-be99e3cd41cce0185805)
