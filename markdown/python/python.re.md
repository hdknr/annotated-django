## トークン化

- [Efficiently split a string using multiple separators and retaining each separator?](https://stackoverflow.com/questions/13186067/efficiently-split-a-string-using-multiple-separators-and-retaining-each-separato)


## アサーション

1.  `(?=...)` :先読みアサーション(lookahead assertion)
2.  `(?!...)` : 否定先読みアサーション(negative lookahead assertion)
3.  `(?<=...)` : 肯定後読みアサーション(positive lookbehind assertion)
4.  `(?<!...)` : 否定後読みアサーション(negative lookbehind assertion)

Python は 先読み(1とに)しか実装していない


~~~py
re.search(r'(\d)(?=(\d{3})+(?!\d))', str(123456789)).groups()
('3', '789')
~~~


## 空白区切り

~~~py
In [17]: print a
a b c　d　あ

In [18]: a
Out[18]: u'a b c\u3000d\u3000\u3042'

In [19]: re.split(ur"[\s\u3000]", a)
Out[19]: [u'a', u'b', u'c', u'd', u'\u3042']
~~~


## 空白置換

~~~py
In [10]: re.sub(ur'[\u3000\s]', '-', u'　　　　　')
Out[10]: u'-----'
~~~
