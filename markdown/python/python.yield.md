## ジェネレータ

- `return` は使えません(`yield`と`return`は同居できない)

~~~py
In [1]: def gen():
   ...:     yield 1
   ...:     yield 2
   ...:     

In [2]: g = gen()

In [3]: g
Out[3]: <generator object gen at 0x7f9ae8092dc0>
~~~

~~~py
In [4]: g.next()
Out[4]: 1

In [5]: type(g)
Out[5]: generator

In [6]: g.next()
Out[6]: 2

In [7]: g.next()
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-7-d7e53364a9a7> in <module>()
----> 1 g.next()

StopIteration:
~~~


## 記事

- [5.5. Iterator Types](https://docs.python.org/2/library/stdtypes.html#iterator-types)
- [Pythonのイテレータとジェネレータ](http://qiita.com/tomotaka_ito/items/35f3eb108f587022fa09)
