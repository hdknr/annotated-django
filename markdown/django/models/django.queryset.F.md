## 全角、半角、大文字小文字区別せずに検索

- `utf8_unicode_ci` 照合順序で検索する

~~~py
In [11]: from django.db.models import Func, F
In [11]: name_ci = Func('name', function='utf8_unicode_ci',  template='(%(expressions)s) COLLATE "%(function)s"')
In [11]: OfficeMaster.objects.annotate(name_ci=name_ci).filter(name_ci__startswith='y').count()
Out[11]: 13

In [12]: OfficeMaster.objects.filter(name__startswith='y').count()                                                                                                         
Out[12]: 0

In [13]: OfficeMaster.objects.filter(name__startswith='Y').count()
Out[13]: 8

In [14]: OfficeMaster.objects.filter(name__startswith=u'Ｙ').count()                                                                                                                
Out[14]: 5
~~~
