unique=True のフィールドの追加マイグレーション

## md5 フィールドを追加

- `path` フィールドの `md5` 値を持たせる

~~~py
class Category(models.Model):
    path = models.CharField(max_length=500, unique=True)
    md5 =  models.CharField(max_length=32, unique=True, db_index=True)
    ...
~~~    

## 0003

~~~bash
$ python manage.py makemigrations categories

You are trying to add a non-nullable field 'md5' to category without a default;
we cant do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> timezone.now()
Migrations for 'categories':
  migrations/0003_category_md5.py:
    - Add field md5 to category
~~~

- 0003

~~~py
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20160906_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='md5',
            field=models.CharField(
                db_index=True,
                default=datetime.datetime(2016, 9, 6, 11, 22, 1, 204471, tzinfo=utc),
                max_length=32, unique=True),
            preserve_default=False,
        ),
    ]
~~~    

## 0004

~~~bash
$ python manage.py makemigrations categories  --empty
~~~

~~~py
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_category_md5'),
    ]

    operations = [
    ]
~~~

## 0005

~~~bash
$ python manage.py makemigrations categories  --empty
~~~

~~~py
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_auto_20160906_1129'),
    ]

    operations = [
    ]
~~~

## 0005: null=True -> unique=True


~~~py
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_auto_20160906_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='md5',
            field=models.CharField(
                db_index=True, max_length=32, unique=True),
            preserve_default=False,
        ),
    ]
~~~

## 0003: null=True

~~~py
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20160906_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='md5',
            field=models.CharField(
                db_index=True,
                max_length=32, null=True),
            preserve_default=False,
        ),
    ]

~~~

## 0004: 値を埋める

~~~py
from __future__ import unicode_literals

from django.db import migrations
from hashlib import md5


def gen_md5(apps, schema_editor):
    Category = apps.get_model('categories', 'Category')
    for category in Category.objects.all():
        category.md5 = md5(category.path).hexdigest()
        category.save()


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_category_md5'),
    ]

    operations = [
        migrations.RunPython(
            gen_md5, reverse_code=migrations.RunPython.noop),
    ]
~~~


## 実行

~~~bash
$ python manage.py migrate categories
Operations to perform:
  Apply all migrations: categories
Running migrations:
  Rendering model states... DONE
  Applying categories.0003_category_md5... OK
  Applying categories.0004_auto_20160906_1129... OK
  Applying categories.0005_auto_20160906_1129... OK
~~~
