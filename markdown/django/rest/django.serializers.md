# jq コマンドでCSV化する

~~~bash
$ python manage.py dumpdata auth.group | jq -r ".[] |[.pk , .fields.name]| @csv"
~~~
