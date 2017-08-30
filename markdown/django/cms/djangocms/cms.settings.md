## 設定

### settings.INSTALLED_APPS

- [サードパーティアプリ](cms.3rdparty.md)

必須:

- 'django.contrib.sites': settings.SITE_ID = 1 の設定
- 'cms' : django-cms
- 'menus': django-cms
- 'treebeard': [django-treebeard](http://django-treebeard.readthedocs.io/en/latest/)


### settings.LANGUAGES


~~~py
gettext = lambda s: s
...
LANGUAGES = (
    ## Customize this
    ('ja', gettext('ja')),
)
~~~

### settings.DATABASES

推奨:

~~~bash
$ pip install psycopg2     # for Postgres
$ pip install mysqlclient  # for MySQL
~~~


### 設定確認



~~~bash
$ python manage.py cms check

********************************
Checking django CMS installation
********************************

Sekizai
=======

  - Sekizai is installed [OK]
  - Sekizai template context processor is installed [OK]
  - Sekizai namespaces 'js' and 'css' found in 'fullwidth.html' [OK]
  - Sekizai namespaces 'js' and 'css' found in 'sidebar_left.html' [OK]
  - Sekizai namespaces 'js' and 'css' found in 'sidebar_right.html' [OK]

Sekizai configuration okay [OK]

Internationalization
====================

  - New style CMS_LANGUAGES [OK]

Middlewares
===========


Context processors
==================


Deprecated settings
===================

  - No deprecated settings found [SKIP]

Plugin instances
================

  - Plugin instances of 1 types found in the database [OK]

The plugins in your database are in good order [OK]

Presence of "copy_relations"
============================


All plugins and page/title extensions have "copy_relations" method if needed. [OK]


OVERALL RESULTS
===============

1 checks skipped!
10 checks successful!

Installation okay
~~~

### `sekizai` 設定

- [sekizai設定](cms.sekizai.md)

### MIDDLEWARE

[MIDDLEWARE](cms.middleware.md) の設定

### Context processors

- [TEMPLATESのコンテキストプロセッサ設定](cms.context_processors.md)

### レイアウト

- [テンプレート](cms.templates.md) の設定


### media/static

- [メディアファイル](cms.media.md)
- [スタティックファイル](cms.static.md)


### ファイル/画像

- [ファイラー](cms.filter.md)


### HTML編集

- [CKEditor](cms.ckeditor.md)

### よく使われるプラグイン

- [基本プラグイン](cms.plugin.md)
