- https://github.com/divio/django-filer ([docs](https://django-filer.readthedocs.io/en/latest/))


## 依存

- https://github.com/SmileyChris/easy-thumbnails  (サムネール)
- https://django-polymorphic.readthedocs.io/en/stable/
- https://github.com/django-mptt/django-mptt/
- https://pillow.readthedocs.io/en/4.2.x/
- https://github.com/avian2/unidecode


## インストール

~~~bash
$ pip install django-filer
~~~

## settings


~~~py
INSTALLED_APPS = [
    ...
    'filer',
    'easy_thumbnails',
    'mptt',
    ...
]
~~~

サムネール関連:

~~~py
THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)
~~~

## マイグレーション

~~~bash
$ python manage.py migrate filer
$ python manage.py migrate easy_thumbnails
~~~
