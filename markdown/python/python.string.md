
# string

- [6.1. string — 一般的な文字列操作 — Python 3.6.5 ドキュメント](https://docs.python.jp/3/library/string.html)

## 'cp932' codec can't encode character u'\u2014' in position 9: illegal multibyte sequence

- [ダッシュ](https://ja.wikipedia.org/wiki/%E3%83%80%E3%83%83%E3%82%B7%E3%83%A5_(%E8%A8%98%E5%8F%B7)#.E7.94.A8.E6.B3.95)
- [str.encode](http://docs.python.jp/2/library/stdtypes.html#str.encode)

~~~py
s.encode('cp932', errors='ignore')
~~~

## format

- [Python3での文字列フォーマットまとめ　旧型で生きるか、新型で生きるか - Qiita](https://qiita.com/u_kan/items/2a7b4201beb0d467e5b8)
- [PyFormat: Using % and .format() for great good!](https://pyformat.info/)

### ゼロ埋める

~~~py
In [1]: i = 30

In [2]: "{:05d}".format(i)
Out[2]: '00030'
~~~

## フォーマット済み文字列リテラル（ formatted string literal / f-string

- [2.4.3. フォーマット済み文字列リテラル](https://docs.python.org/ja/3/reference/lexical_analysis.html#f-strings)
- [PEP 498 -- Literal String Interpolation | Python.org](https://www.python.org/dev/peps/pep-0498/)
- [The new f-strings in Python 3.6 | Seasoned & Agile](https://cito.github.io/blog/f-strings/)
- [Python 3's f-Strings: An Improved String Formatting Syntax (Guide) – Real Python](https://realpython.com/python-f-strings/)

## 論理値

~~~python
In [37]: from distutils.util import strtobool
In [38]: strtobool('TRUE')
Out[38]: 1
~~~

- [django.db.models.fields.BooleanField では "TRUE" / "FALSE"はエラー](https://github.com/hdknr/annotated-django/commit/69d84147fad6719a61502102bd7f8a69d132232d)


## 中国語

- [hanziconv](https://pypi.python.org/pypi/hanziconv/)

## i18n

- [gettext plural rules - built from CLDR](http://mlocati.github.io/cldr-to-gettext-plural-rules/)
