## static finders

~~~py
In [1]: from django.contrib.staticfiles.finders import get_finders

In [2]: for finder in get_finders():
   ...:     print(finder)
   ...:
<django.contrib.staticfiles.finders.FileSystemFinder object at 0x7fbf0ea5a390>
<django.contrib.staticfiles.finders.AppDirectoriesFinder object at 0x7fbf0ea5a400>
~~~

~~~py
In [3]: list(get_finders())[1]
Out[3]: <django.contrib.staticfiles.finders.AppDirectoriesFinder at 0x7fbf0ea5a400>
In [4]: finder = _

~~~

~~~py
In [6]: for path, storage in finder.list([]):                                                                               
   ...:     print(path, storage) ...:                                                                                                                                                       
admin/fonts/LICENSE.txt <django.core.files.storage.FileSystemStorage object at 0x7fbf0ea5a470>                              
admin/fonts/Roboto-Bold-webfont.woff <django.core.files.storage.FileSystemStorage object at 0x7fbf0ea5a470>                                                                  
admin/fonts/Roboto-Regular-webfont.woff <django.core.files.storage.FileSystemStorage object at 0x7fbf0ea5a470>               
~~~

~~~py
In [7]: list(finder.list([]))[0]
Out[7]:
('admin/fonts/LICENSE.txt',
 <django.core.files.storage.FileSystemStorage at 0x7fbf0ea5a470>)
~~~

### アプリケーションのディレクトリを見つける

~~~py
In [1]: from django.apps import apps

In [2]: configs = apps.get_app_configs()
In [3]: type(configs)
Out[3]: odict_values

In [4]: list(iter(configs))[0]
Out[4]: <AdminConfig: admin>
In [5]: conf = _

In [6]: import os
In [7]: path = os.path.join(conf.path, 'static')
In [8]: path
Out[8]: '/home/vagrant/.anyenv/envs/pyenv/versions/cms/lib/python3.6/site-packages/django/contrib/admin/static'
~~~


## staticfiles_storage

~~~py
In [15]: from django.contrib.staticfiles.storage import staticfiles_storage

In [16]: staticfiles_storage.path('categories/okinawa/favicon.ico')
Out[16]: '/vagrant/projects/hdknr/mysite3/web/static/categories/okinawa/favicon.ico'
~~~

~~~bash
$ cat /tmp/hello.txt
Hello, Static Files.
~~~

コピー:

~~~py
In [17]: from django.core.files import File

In [18]: File(open('/tmp/hello.txt', 'rb'))
Out[18]: <File: /tmp/hello.txt>

In [19]: staticfiles_storage.save('categories/okinawa/hello.txt', _)
Out[19]: 'categories/okinawa/hello.txt'

In [22]: File(open(staticfiles_storage.path('categories/okinawa/hello.txt')))
Out[22]: <File: /vagrant/projects/hdknr/mysite3/web/static/categories/okinawa/hello.txt>


In [23]: _.read()
Out[23]: 'Hello, Static Files.\n'
~~~

デフォルトで別名になる:


~~~py
In [25]: staticfiles_storage.save('categories/okinawa/hello.txt', File(open('/tmp/hello.txt', 'rb')))
Out[25]: 'categories/okinawa/hello_7ZzSOHS.txt'

In [26]: staticfiles_storage.save('categories/okinawa/hello.txt', File(open('/tmp/hello.txt', 'rb')))
Out[26]: 'categories/okinawa/hello_EsLmd58.txt'
~~~

削除してから:

~~~py
In [29]: staticfiles_storage.delete('categories/okinawa/hello.txt')

In [30]: staticfiles_storage.save('categories/okinawa/hello.txt', File(open('/tmp/hello.txt', 'rb')))
Out[30]: 'categories/okinawa/hello.txt'
~~~

##  STATICFILES_STORAGE

~~~py
STATICFILES_STORAGE = 'mymedia.storages.locals.StaticStorage'
~~~
