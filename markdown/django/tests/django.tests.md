## Django Testing

- [Testing in Django](https://docs.djangoproject.com/en/1.8/topics/testing/)
- [Testing tools](https://docs.djangoproject.com/en/1.8/topics/testing/tools/)
- [Advanced testing topics](https://docs.djangoproject.com/en/1.8/topics/testing/advanced/)
- [Python Test cases](https://docs.python.org/3/library/unittest.html#test-cases)
- [Django Testing Docs](http://django-testing-docs.readthedocs.io/en/latest/index.html)
- [Djangoでテストコードを書く](https://codelab.website/django-testcode/) (`django-nose` + `coverage`)


### 実行

- [Writing and running tests](https://docs.djangoproject.com/en/1.8/topics/testing/overview/)

~~~
$ ./manage.py test
~~~

## モジュールテスト

- [Using the Django test runner to test reusable applications](https://docs.djangoproject.com/en/1.11/topics/testing/advanced/#using-the-django-test-runner-to-test-reusable-applications)

## `--keepdb` :データベースを削除させない

- 事前に test_{{ 実際のデータベース名 }} を作成する

~~~bash
$ python manage.py test yourapp --keepdb
~~~


## Content Type fixture

- 作成

~~~
$ ./manage.py dumpdata contenttypes --indent 2
~~~

- content type なし

~~~
$ ./manage.py dumpdata --exclude contenttypes
~~~

## auth.permissionでハマるので

~~~
$ ./manage.py dumpdata --natural --exclude auth.permission --exclude contenttypes --indent 4  
~~~



## 無駄なテストを実行しない

- [cyberj/django-ignoretests](https://github.com/cyberj/django-ignoretests)