## 'cp932' codec can't encode character u'\u2014' in position 9: illegal multibyte sequence

- [ダッシュ](https://ja.wikipedia.org/wiki/%E3%83%80%E3%83%83%E3%82%B7%E3%83%A5_(%E8%A8%98%E5%8F%B7)#.E7.94.A8.E6.B3.95)
- [str.encode](http://docs.python.jp/2/library/stdtypes.html#str.encode)

~~~py
s.encode('cp932', errors='ignore')
~~~
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
