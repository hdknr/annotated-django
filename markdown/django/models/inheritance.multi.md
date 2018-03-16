## 複数の多重継承元でフィールドが被っていると、モデルの初期化した時に値が飛んでしまう問題

~~~py
class A(models.Model):
    version = models.CharField(max_length=10)
    a = models.CharField(max_length=10)
    class Meta:
        abstract = True

    def __str__(self):
        return 'a'

class AA(A):
    class Meta:
        abstract = True

    def __str__(self):
        return 'aa'

class B(models.Model):
    version = models.CharField(max_length=10)
    b = models.CharField(max_length=10)
    class Meta:
        abstract = True

    def __str__(self):
        return 'b'

class C(A, B):
    c = models.CharField(max_length=10)
    class Meta:
        abstract = True

    def __str__(self):
        return 'c'
~~~

versionは A で定義されていて、継承している

~~~py
In [2]: AA(version="333")
Out[2]: <AA: aa>

In [4]: _.version
Out[4]: '333'
~~~

version は AとCで定義されている。おそらく Aでの初期化(__init__)のあとで、Bの初期化(__init__)が行われる:

~~~py
In [5]: C(version="444")
Out[5]: <C: c>

In [6]: _.version
Out[6]: ''
~~~


メタクラスを定義して、親クラスをmodels.Model に変更し、その代わり元の親クラスのフィールドをattrsに移動する:

~~~py
from django.db.models.base import ModelBase

class Cx(ModelBase):

    def __new__(cls, name, bases, attrs):
        modelbases = filter(lambda b: issubclass(b, models.Model), bases)
        for base in modelbases:
            for field in base._meta.fields:
                attrs[field.name] = field
        bases = tuple(filter(lambda b: not issubclass(b, models.Model), bases)) + (models.Model, )
        return super().__new__(cls, name, bases, attrs)


class CC(A, B, metaclass=Cx):
    cc = models.CharField(max_length=10)

    class Meta:
        abstract = True

    def __str__(self):
        return 'c'
~~~

~~~py
In [2]: CC(version='hoge')
Out[2]: <CC: c>

In [3]: _.version
Out[3]: 'hoge'
~~~
