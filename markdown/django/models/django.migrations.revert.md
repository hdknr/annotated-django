マイグレーションを戻す

~~~bash
$ python manage.py showmigrations products
products
 [X] 0001_initial
 [X] 0002_auto_20160906_1240
 [X] 0003_auto_20160906_1241
 [X] 0004_product_company
 [X] 0005_auto_20160907_0524
 [X] 0006_auto_20160907_0524
 [X] 0007_dummy
~~~

~~~bash
$ python manage.py migrate products 0006

Operations to perform:
  Target specific migration: 0006_auto_20160907_0524, from products
Running migrations:
  Rendering model states... DONE
  Unapplying products.0007_dummy... OK
The following content types are stale and need to be deleted:

    products | dummy

Any objects related to these content types by a foreign key will also
be deleted. Are you sure you want to delete these content types?
If you are unsure, answer 'no'.

    Type 'yes' to continue, or 'no' to cancel: yes
~~~

~~~bash
$  python manage.py showmigrations products
products
 [X] 0001_initial
 [X] 0002_auto_20160906_1240
 [X] 0003_auto_20160906_1241
 [X] 0004_product_company
 [X] 0005_auto_20160907_0524
 [X] 0006_auto_20160907_0524
 [ ] 0007_dummy
~~~

~~~bash
$ rm products/migrations/0007_dummy.py
~~~

~~~bash
$ python manage.py showmigrations products
products
 [X] 0001_initial
 [X] 0002_auto_20160906_1240
 [X] 0003_auto_20160906_1241
 [X] 0004_product_company
 [X] 0005_auto_20160907_0524
 [X] 0006_auto_20160907_0524
~~~

- レポジトリから戻したりとか。。。。

~~~bash
$ python manage.py makemigrations products
No changes detected in app 'products'
~~~
