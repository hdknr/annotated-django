
- http://docs.python.jp/2/library/functions.html#reduce
- [何気にPythonでつかっていた関数型プログラミング技法いろいろ](http://qiita.com/HirofumiYashima/items/769656130111ef7b2f7e)

## ファイルのパスを作る

~~~py
In [28]: reduce(lambda i, j: ['/'] if i == '' else i + [i[-1] +  j + '/'], ['', '', 'a', 'b', 'c'])
Out[28]: ['/', '/a/', '/a/b/', '/a/b/c/']
~~~

## モデルフィールド名のマッパーを作る

- verbose_name あるいは name の存在チェックする
- フィールドリストの先頭をからの配列(`[]`)にすることで `array` の初期値を与える

~~~py
def get_mapper(self):                                                           
    return dict(                                                                
        reduce(                                                                 
            lambda array, y: array + [(y.verbose_name, y.name), (y.name, y.name)],   
            [[]] + list(self.opt.fields)))         
~~~
