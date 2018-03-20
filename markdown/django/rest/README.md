[#36](https://github.com/hdknr/annotated-django/issues/36)

- [ビューセット](drf.viewsets.md)

## シリアリアザ

- [シリアライザ](drf.serializers.md)
- [ネストしたシリアライザ](drf.serializers.nested.md)
- [抽象モデル](drf.serializers.abstract.md)

## requests

- [SHIFT_JISでPOSTする](requests.md)

## curl

- [curlコマンドから HTTP POST する方法
](https://qiita.com/letsspeak/items/8c7266742371699ab45e)

FORM:

~~~bash
$ curl -F "name1=value1" -F "name2=value2" http://yourdomain/execute.script
~~~

JSON:

~~~bash
$ curl -X POST -H "Content-Type: application/json" -d '
{
    "name": "Manager",
    "description": "someone who manages"
}'
~~~
