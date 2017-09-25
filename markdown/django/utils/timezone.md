- [python datetime](../../python/python.datetime.md)

## localtime(dt)

- is_aware な DateTimeを localtime に変換する

~~~py
In [2]: from django.utils.timezone import *
In [3]: now()
Out[3]: datetime.datetime(2017, 9, 25, 5, 18, 28, 195976, tzinfo=<UTC>

In [4]: localtime(_)
Out[8]: datetime.datetime(2017, 9, 25, 14, 18, 28, 195976, tzinfo=<DstTzInfo 'Asia/Tokyo' JST+9:00:00 STD>)

In [9]: _.strftime('%Y-%m-%d %H:%M:%S')
Out[9]: '2017-09-25 14:18:28'
~~~
