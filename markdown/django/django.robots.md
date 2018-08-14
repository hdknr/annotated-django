- https://django-robots.readthedocs.io/en/latest/
- https://github.com/jazzband/django-robots


## 設置



app/settings.py:

~~~py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,     #  django.template.loaders.app_directories.Loader
        ...
    },
]

INSTALLED_APPS += [
    'django.contrib.sites',
    'django.contrib.sitemaps',
    ...
    'robots',
    ...
]
SITE_ID = 1
~~~

migrate:

~~~bash
$ python manage.py migrate
~~~

~~~bash
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, histories, mylinks, robots, sessions, sites, taggit
Running migrations:
  Applying sites.0001_initial... OK
  Applying robots.0001_initial... OK
  Applying sites.0002_alter_domain_unique... OK
~~

app/urls.py:

~~~py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('robot.txt', include('robots.urls')),
    path('admin/', admin.site.urls),
]
~~~

確認:

~~~bash
$ curl http://localhost:9900/robot.txt

User-agent: *
Disallow:

Host: example.com
~~~

## サンプルのフィックスチャ

~~~bash 
$ python manage.py dumpdata --indent 2 robots
~~~

~~~json
[
{
  "model": "robots.url",
  "pk": 1,
  "fields": {
    "pattern": "/admin"
  }
},
{
  "model": "robots.url",
  "pk": 2,
  "fields": {
    "pattern": "/"
  }
},
{
  "model": "robots.rule",
  "pk": 1,
  "fields": {
    "robot": "*",
    "crawl_delay": null,
    "allowed": [],
    "disallowed": [
      1
    ],
    "sites": [
      1
    ]
  }
},
{
  "model": "robots.rule",
  "pk": 2,
  "fields": {
    "robot": "Googlebot",
    "crawl_delay": null,
    "allowed": [
      2
    ],
    "disallowed": [],
    "sites": [
      1
    ]
  }
}
]
~~~

url テーブルに URLパターンを登録:

~~~sql
CREATE TABLE "robots_url" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "pattern" varchar(255) NOT NULL);
~~~


rule テーブルにBOTを登録:

~~~sql
CREATE TABLE "robots_rule" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "robot" varchar(255) NOT NULL, 
    "crawl_delay" decimal NULL);
~~~

ルールの実際の定義はManyToManyフィールドで管理されている:

- `robots_rule_allowed`
- `robots_rule_disallowed`
- `robots_rule_sites`

## リソース

- [Robots Database:robotstxt.org](http://www.robotstxt.org/db.html)
- [robots.txt ファイルを作成する](https://support.google.com/webmasters/answer/6062596?hl=ja)

## 実際の例


- [facebook](https://facebook.com/robots.txt)