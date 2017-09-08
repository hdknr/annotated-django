# MySQL関連

## TRUNCATE TABLE

~~~
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE table1;
SET FOREIGN_KEY_CHECKS = 1;
~~~


## mysqlclient

- https://github.com/PyMySQL/mysqlclient-python

~~~bash
$ pip install mysqlclient
~~~

settings.py:

~~~py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        ...
    }
}
~~~


## データベース作成

jinja2:

~~~mysql
CREATE DATABASE {{ NAME}}
DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
GRANT ALL on {{ NAME }}.*
to '{{ USER }}'@'{{ SOURCE }}'
identified by '{{ PASSWORD }}' WITH GRANT OPTION;
~~~

~~~bash
$ pip install jinja2-cli
~~~

~~~bash
$ jinja2 -D NAME=dbname -D USER=dbuser -D PASSWORD=dbpassword -D SOURCE=localhost ~/createdb.sql
~~~
