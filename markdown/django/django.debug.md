# Debug

- [#37](https://github.com/hdknr/annotated-django/issues/37)

## pdb

- [27.3. pdb — Python デバッガ](https://docs.python.jp/3/library/pdb.html)
- [pdb: Using the Python debugger in Django](https://mike.tig.as/blog/2010/09/14/pdb/)

ブレークさせる:

~~~py
import pdb; pdb.set_trace()     
~~~

変数の表示( [27.3.1. デバッガコマンド](https://docs.python.jp/3/library/pdb.html#debugger-commands)):

~~~
(Pdb) p value

OrderedDict([('tags', ['Photo']), ('title', 'br3'), ('access', 'public')])              
~~~



## コールスタック

~~~
import inspect
print inspect.stack()
~~~



## Exception

- [Django Exceptions](https://docs.djangoproject.com/ja/1.9/ref/exceptions/)
