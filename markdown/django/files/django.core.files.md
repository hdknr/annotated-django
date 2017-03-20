Django Files

- [The File object](https://docs.djangoproject.com/ja/1.9/ref/files/file/)

## テキストをファイルに保存する

~~~py
from django.core.files.storage import get_storage_class
from django.core.files.base import ContentFile

get_storage_class()().save('log.txt', ContentFile('something to log'))
~~~


~~~py
In [1]: from django.core.files.storage import get_storage_class
   ...:

In [2]: get_storage_class()
Out[2]: django.core.files.storage.FileSystemStorage
~~~
