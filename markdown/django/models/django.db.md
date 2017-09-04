## cursor

- [Executing custom SQL directly](https://docs.djangoproject.com/en/1.11/topics/db/sql/#executing-custom-sql-directly)

~~~py
In [1]: from django.db import connection

In [2]: connection.cursor()
Out[2]: <django.db.backends.utils.CursorDebugWrapper at 0x7f1c85da79d0>

In [3]: db = _

In [4]: db.execute('select * from auth_user')
Out[4]: 37048L

In [12]: res = db.fetchall()

In [13]: type(res)
Out[13]: tuple

In [14]: len(res)
Out[14]: 37048

In [15]: res = db.fetchall()

In [16]: len(res)
Out[16]: 0
~~~


CursorDebugWrapper:

メソッド      |  SQL        | 内容
-------------|-------------|--------------------------------------
fetchone()   | FETCH NEXT  | 現在行から１行取得し、次の行へ
fetchmany(n) | FETCH FORWARD n | 現在行からn行取得し、次の行へ
fetchall()   | FETCH ALL   | 現在行から残り全行を取得し、次の行へ
scroll(value, mode) | MOVE | mode=relative: alueで指定された変分だけ移動, mode=absolute: value=0は先頭行、value=-1は最終行


## backends

- [mysql](django.mysql.md)
