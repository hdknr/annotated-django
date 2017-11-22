## elasticsearch-py

~~~bash
$ pip install elasticsearch
~~~

- [elasticsearch-py](https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/index.html)
- [RTD](https://elasticsearch-py.readthedocs.io/en/master/#)

接続:
~~~py
In [1]: from elasticsearch import Elasticsearch
In [2]: es = Elasticsearch()
~~~

データ登録:
~~~py
In [3]: from datetime import datetime
In [4]: es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})
Out[4]:
{'_id': '42',
 '_index': 'my-index',
 '_primary_term': 1,
 '_seq_no': 0,
 '_shards': {'failed': 0, 'successful': 1, 'total': 2},
 '_type': 'test-type',
 '_version': 1,
 'result': 'created'}
~~~

検索:
~~~py
 In [5]: es.get(index="my-index", doc_type="test-type", id=42)['_source']
 Out[5]: {'any': 'data', 'timestamp': '2017-11-22T22:00:30.466155'}
~~~

curlで確認: [Elasticsearchを使ってみる](https://qiita.com/reoring/items/c91cca84854ceaca3589)

~~~bash
$ curl -XGET http://taberu.local:9200/my-index/test-type/42?pretty=true
~~~
~~~js
{
  "_index" : "my-index",
  "_type" : "test-type",
  "_id" : "42",
  "_version" : 1,
  "found" : true,
  "_source" : {
    "any" : "data",
    "timestamp" : "2017-11-22T22:00:30.466155"
  }
}
~~~

## elasticsearch-dsl

~~~bash
$ pip install elasticsearch-dsl
~~~

- [Elasticsearch DSL](http://elasticsearch-dsl.readthedocs.io/en/latest/)
- [Python elasticsearch-dsl django pagination](http://stackoverflow.com/questions/35880868/python-elasticsearch-dsl-django-pagination)
- [PythonからElasticsearchを扱うelasticsearch-dsl-pyがなかなか良かった](http://bit.ly/2dazJOy)

## django

- [liberation/django-elasticsearch](https://github.com/liberation/django-elasticsearch)
- [ytyng/django-elasticindex](https://github.com/ytyng/django-elasticindex)
-  [rangertaha/django-elastic](https://github.com/rangertaha/django-elastic )
- [asyncee/django-el](https://github.com/asyncee/django-el)
