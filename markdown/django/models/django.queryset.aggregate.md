# Aggregate

## datetimeフィールドの日付で件数を出す

- [extra](https://docs.djangoproject.com/en/1.8/ref/models/querysets/#django.db.models.query.QuerySet.extra) で `last` (date) を追加する

~~~py
>>> Profile.objects.extra({'last': "date(updated)"})[0].last
datetime.date(2015, 2, 10)
>>> Profile.objects.extra(select={'last': "date(updated)"})[0].last
datetime.date(2015, 2, 10)
~~~

~~~py
>>> type(Profile.objects.extra(select={'last': 'date(updated)'}))
<class 'django.db.models.query.QuerySet'>
~~~


- dateはMySQL(sqliteも)の関数

~~~
mysql> select date(updated) as last from accounts_profile limit 1;
+------------+
| last       |
+------------+
| 2015-02-10 |
+------------+
1 row in set (0.00 sec)
~~~

- ValueQuerySet

~~~py
>>> type(Profile.objects.extra(select={'last': 'date(updated)'}).values('last'))
<class 'django.db.models.query.ValuesQuerySet'>
~~~

- ValueQuerSetを件数で集約する
- `last` で descソートする

~~~py
>>> from django.db.models import Count
>>> Profile.objects.extra({'last': "date(updated)"}).values('last').annotate(count=Count('id')).order_by('-last')
>>> c = _
>>> for i in c:
...     print i['last'], i['count']
...
2015-09-25 7096
2015-06-16 198
2015-05-01 1
~~~

## Status を別テーブルで持っている

~~~py
In [1]: from wares.models import *
In [2]: from django.db.models import Count

In [5]: WareOrder.objects.all().values('status', 'status__name').annotate(total=Count('status')).order_by('total')
Out[5]: <QuerySet [{'status': None, 'total': 0, 'status__name': None}, {'status': 6L, 'total': 13, 'status__name': u'\u767a\u9001\u6e96\u5099\u4e2d'}]>
~~~

## 記事

- [Djangoの集計について](http://note.crohaco.net/2014/django-aggregate/)
- [django - Annotating a Sum results in None rather than zero - Stack Overflow](https://stackoverflow.com/questions/6160648/annotating-a-sum-results-in-none-rather-than-zero)
