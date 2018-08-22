# ヘッダー

## サブジェクトのデコード

- [decode_header()](https://docs.python.jp/3/library/email.header.html#email.header.decode_header)

~~~py
In [1]: from email.header import decode_header

In [2]: type(m.mailobject)
Out[2]: email.message.Message

In [3]: src, enc = decode_header(m.mailobject.get('subject'))[0]

In [4]: src.decode(enc)
Out[4]: 'Wantedlyにようこそ！'
~~~