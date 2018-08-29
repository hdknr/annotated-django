- https://github.com/joke2k/faker


## 使い方

[rtd](https://faker.readthedocs.io/en/latest/):

~~~py 
In [1]: from faker import Faker
In [2]: lang = 'ja_JP'
In [3]: fake = Faker(lang)
In [5]: fake.name()
Out[5]: '鈴木 太郎'
~~~

## コマンド

~~~bash
$ faker -l ja_JP address

山形県武蔵野市卯の里23丁目18番10号 パーク渡辺280
~~~

## ロケール

- [ja_JP](https://faker.readthedocs.io/en/latest/locales/ja_JP.html)
- [Change default faker locale in factory_boy](https://stackoverflow.com/questions/45773954/change-default-faker-locale-in-factory-boy)

~~~py
name = factory.Faker('first_name', locale='es_ES')
~~~

[override_default_locale](https://factoryboy.readthedocs.io/en/latest/reference.html?highlight=override_default_locale#factory.Faker.override_default_locale):

~~~py
>>> with factory.Faker.override_default_locale('de_DE'):
...     UserFactory()
<User: Johannes Brahms>
~~~

~~~py
@factory.Faker.override_default_locale('es_ES')
def test_foo(self):
    user = ExampleFactory()
~~~


##　記事

- [faker – Fakerは、あなたのために偽のデータを生成するPythonパッケージ](https://githubja.com/joke2k/faker)