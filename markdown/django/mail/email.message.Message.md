# email.message.Message

- [19.1.1. email.message: 電子メールメッセージの表現 — Python 3.6.6 ドキュメント](https://docs.python.org/ja/3/library/email.message.html)
- [19.1.2. email.parser: 電子メールメッセージのパース — Python 3.6.6 ドキュメント](https://docs.python.org/ja/3/library/email.parser.html)


メール本体:

~~~py
In [1]: type(m.mailobject)
Out[1]: email.message.Message
~~~

マルチパート
~~~py
In [1]: parts = list(m.mailobject.walk())
~~~

~~~py
In [1]: [part.get_content_type() for part in parts]
Out[1]: ['multipart/alternative', 'text/plain', 'text/html']
~~~

index = 0 : 本体:

~~~py
In [1]: parts[0]
Out[1]: <email.message.Message at 0x7f6bb9f534a8>
~~~

~~~py
In [1]: parts[0] == m.mailobject
Out[1]: True
~~~

それぞれのパート:

~~~py
In [0]: list(parts[0].walk())
Out[0]: 
[<email.message.Message at 0x7f6bb9f534a8>,
 <email.message.Message at 0x7f6bb9f53fd0>,
 <email.message.Message at 0x7f6bb9f53d30>]

In [1]: list(parts[1].walk())
Out[1]: [<email.message.Message at 0x7f6bb9f53fd0>]

In [2]: list(parts[2].walk())
Out[2]: [<email.message.Message at 0x7f6bb9f53d30>]
~~~

ただし、:

~~~py
In [1]: [part.is_multipart()  for part in parts]
Out[1]: [True, False, False]
~~~