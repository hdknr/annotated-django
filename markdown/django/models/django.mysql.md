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
