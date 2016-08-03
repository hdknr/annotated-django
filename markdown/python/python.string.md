## format


### ゼロ埋める

~~~py
In [1]: i = 30

In [2]: "{:05d}".format(i)
Out[2]: '00030'
~~~


## 論理値

~~~python
In [37]: from distutils.util import strtobool
In [38]: strtobool('TRUE')
Out[38]: 1
~~~

- [django.db.models.fields.BooleanField では "TRUE" / "FALSE"はエラー](https://github.com/hdknr/annotated-django/commit/69d84147fad6719a61502102bd7f8a69d132232d)
