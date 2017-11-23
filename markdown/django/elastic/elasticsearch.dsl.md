elasticsearch_dsl: Djangoのモデルと連携

- [elasticsearch_dsl.document](https://github.com/elastic/elasticsearch-dsl-py/blob/master/elasticsearch_dsl/document.py)
- [RTD](http://elasticsearch-dsl.readthedocs.io/)

## 基本

Elasticsearch + DSL Search
~~~py
In [1]: from elasticsearch import Elasticsearch
In [2]: from elasticsearch_dsl import Search
~~~

Search:
~~~py
In [3]: client = Elasticsearch()
In [4]: s = Search(using=client, index="my-index")
In [5]: s
Out[5]: <elasticsearch_dsl.search.Search at 0x7fc96a23d4a8>
~~~

検索条件設定:
~~~py
In [6]: s.query('match', any='data')
Out[6]: <elasticsearch_dsl.search.Search at 0x7fc96a141c88>
In [7]: s = _
~~~

検索実行と結果リスト:
~~~py
In [8]: s.execute()
Out[8]: <Response: [<Hit(my-index/test-type/42): {'any': 'data', 'timestamp': '2017-11-22T22:00:30.466155'}>]>
In [9]: res = _
~~~

Hit(検索結果):

~~~py
In [10]: res[0]
Out[10]: <Hit(my-index/test-type/42): {'any': 'data', 'timestamp': '2017-11-22T22:00:30.466155'}>
In [11]: hit = _
~~~

結果のメタ情報:

~~~py
In [12]: hit.meta
Out[12]: {'index': 'my-index', 'id': '42', 'score': 0.2876821, 'doc_t...}
~~~

結果データ:

~~~py
In [13]: hit.any
Out[13]: 'data'

In [14]: hit.timestamp
Out[14]: '2017-11-22T22:00:30.466155'
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
