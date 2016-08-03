Q オブジェクト

- [Complex lookups with Q objects](https://docs.djangoproject.com/en/1.8/topics/db/queries/#complex-lookups-with-q-objects)

~~~py
from django.db.models import Q
Q(question__startswith='What')
~~~

## AND / OR

- AND

~~~py
In [4]: Q(id=1, is_superuser=True)
Out[4]: <Q: (AND: ('is_superuser', True), ('id', 1))>

In [6]: User.objects.filter(Q(id=1, is_superuser=True))
Out[6]: [<User: admin>]

In [7]: User.objects.filter(Q(id=1, is_superuser=False))                                                                                       
Out[7]: []
~~~

- OR

~~~py
In [8]: Q(id=1)|Q(is_superuser=True)
Out[8]: <Q: (OR: ('id', 1), ('is_superuser', True))>

In [9]: User.objects.filter(Q(id=1)|Q(is_superuser=True))
Out[9]: [<User: admin>, <User: webmaster>, <User: vagrantuser>]
~~~


- 同じフィールドでのAND

~~~py
In [1]: import operator
In [2]: from django.db.models import Q
In [3]: query = reduce(operator.and_, (Q(first_name__contains = item) for item in [u'鈴木', u'一朗']))
In [4]: query
Out[4]: <Q: (AND: ('first_name__contains', u'\u9234\u6728'), ('first_name__contains', u'\u4e00\u6717'))>
~~~
