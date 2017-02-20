
- [Googleカレンダーより日本の休日を取得](https://bitbucket.org/vourja/japanese-holiday)
- [各国の休日](https://github.com/novapost/workalendar)


## iso week

- [pypi/isoweek](https://pypi.python.org/pypi/isoweek) : [gisle/isoweek](https://github.com/gisle/isoweek)

~~~py
In [1]: from isoweek import Week

In [2]: Week(2016, 50)
Out[2]: isoweek.Week(2016, 50)

In [3]: _.monday()
Out[3]: datetime.date(2016, 12, 12)

In [5]: Week(2016, 52)
Out[5]: isoweek.Week(2016, 52)

In [6]: Week(2016, 53)
Out[6]: isoweek.Week(2017, 1)

In [19]: str(Week(2016,1))
Out[19]: '2016W01'


In [24]: Week.fromstring('2015W53').days()
Out[24]:
[datetime.date(2015, 12, 28),
 datetime.date(2015, 12, 29),
 datetime.date(2015, 12, 30),
 datetime.date(2015, 12, 31),
 datetime.date(2016, 1, 1),
 datetime.date(2016, 1, 2),
 datetime.date(2016, 1, 3)]
~~~
