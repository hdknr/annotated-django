
## django-taggit

- [alex/django-taggit](https://github.com/alex/django-taggit)
- [glemmaPaul/django-taggit-serializer](https://github.com/glemmaPaul/django-taggit-serializer)
- [Django Packages: Tagging](https://djangopackages.org/grids/g/tagging/)

## 利用

- [API](http://django-taggit.readthedocs.io/en/latest/api.html)

追加:

~~~py
instance.tags.add("red", "green", "fruit")
~~~

## インストール


~~~bash
$ pip install
~~~

~~~py
INSTALLED_APPS = APPS + INSTALLED_APPS + [                                          
    ....
    'taggit',           # django-taggit    
    ....
~~~    

~~~bash
$ DJ migrate
Operations to perform:
  Apply all migrations: admin, auth,  contenttypes, ...., taggit, ....
Running migrations:
  Applying taggit.0001_initial... OK
  Applying taggit.0002_auto_20150616_2121... OK
~~~

~~~py
from taggit.managers import TaggableManager
from . import defs, methods

class Product(defs.Product, methods.Product):
    ....
    tags = TaggableManager()
~~~    

~~~bash
$ python manage.py makemigrations products
Migrations for 'products':
 products/migrations/0002_product_tags.py:
   - Add field tags to product
~~~

~~~bash
$ python manage.py migrate products
Operations to perform:
  Apply all migrations: products
Running migrations:
  Applying products.0002_product_tags... OK
~~~

~~~bash
$ echo "show tables" | python manage.py dbshell | grep tag
taggit_tag
taggit_taggeditem
~~~

~~~bash
$ echo "desc taggit_tag" | python manage.py dbshell
Field   Type    Null    Key     Default Extra
id      int(11) NO      PRI     NULL    auto_increment
name    varchar(100)    NO      UNI     NULL
slug    varchar(100)    NO      UNI     NULL
~~~

~~~bash
$ echo "desc taggit_taggeditem" | python manage.py dbshell
Field   Type    Null    Key     Default Extra
id      int(11) NO      PRI     NULL    auto_increment
object_id       int(11) NO      MUL     NULL
content_type_id int(11) NO      MUL     NULL
tag_id  int(11) NO      MUL     NULL
~~~
