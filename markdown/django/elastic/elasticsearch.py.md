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

検索:
~~~bash
$ curl -XGET 'http://taberu.local:9200/my-index/_search?q=any:data&pretty=true'
~~~
~~~js
{
  "took" : 3,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 1,
    "max_score" : 0.2876821,
    "hits" : [
      {
        "_index" : "my-index",
        "_type" : "test-type",
        "_id" : "42",
        "_score" : 0.2876821,
        "_source" : {
          "any" : "data",
          "timestamp" : "2017-11-22T22:00:30.466155"
        }
      }
    ]
  }
}
~~~

## マッピングの確認

- [Get Mapping](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-get-mapping.html)

~~~bash
$ curl -XGET http://taberu.local:9200/django/_mapping/contents.content?pretty
~~~
~~~js
{
  "django" : {
    "mappings" : {
      "contents.content" : {
        "properties" : {
          "html" : {
            "type" : "text",
            "fields" : {
              "raw" : {
                "type" : "keyword"
              }
            },
            "analyzer" : "html_strip"
          },
          "title" : {
            "type" : "text"
          }
        }
      }
    }
  }
}
~~~
