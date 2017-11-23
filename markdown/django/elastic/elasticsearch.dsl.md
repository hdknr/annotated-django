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


## ModelDocTypeとModelDocTypeMeta

~~~py
# coding: utf-8
from __future__ import unicode_literals
from django.conf import settings
from elasticsearch_dsl import DocType
from elasticsearch_dsl.document import DocTypeMeta
from core.utils import to_natural_key_string

INDEX = getattr(settings, 'ELASTICSEARCH_INDEX', 'django')

def from_hit(cls, hit):
    return cls._model.objects.get(pk=hit.meta.id)                                 


class ModelDocTypeMeta(DocTypeMeta):
    '''DocTypeMetaのカスタマイズ'''
    def __new__(cls, name, bases, attrs):
        if 'Meta' in attrs and hasattr(attrs['Meta'], 'model'):
            # モデルが定義されていたら、 _modelにセットして、 doc_type, index修正
            attrs['Meta'].doc_type = to_natural_key_string(attrs['Meta'].model)
            attrs['_model'] = attrs['Meta'].model
            attrs['from_hit'] = classmethod(from_hit)
            if not hasattr(attrs['Meta'], 'index'):
                attrs['Meta'].index = INDEX

        return super(ModelDocTypeMeta, cls).__new__(cls, name, bases, attrs)


class ModelDocType(DocType):
    __metaclass__ = ModelDocTypeMeta

    def __init__(self, **kwargs):
        instance = kwargs.pop('instance', None)
        if instance:
            # インスタンスが指定されたら、mappingに定義されているフィールドにコピー
            params = dict(
                (i, getattr(instance, i))
                for i in self._doc_type.mapping)
            params.update(kwargs)
            kwargs = params
        super(ModelDocType, self).__init__(**kwargs)
        if instance:                                                                
            self.meta.id = instance.pk    
~~~

## Product と ProductIndexer

~~~py
# coding: utf-8
from __future__ import unicode_literals
import elasticsearch_dsl as dsl
from . import models
from core.indexers import ModelDocType


class ProductIndexer(ModelDocType):
    code = dsl.String()
    name = dsl.String()
    description = dsl.String()

    class Meta:
        model = models.Product        # モデルを定義


from elasticsearch_dsl.connections import connections
connections.create_connection(hosts=['localhost'], timeout=20)
ProductIndexer.init()
~~~


## 保存

~~~py
In [1]: from products.indexers import *

In [2]: p = ProductIndexer(instance=ProductIndexer._model.objects.last())

In [3]: p._doc_type.name
Out[3]: u'products.product'

In [4]: p.meta.index
Out[4]: u'django'

In [5]: p.meta.id
Out[5]: 3

In [6]: p.save()
Out[6]: True
~~~

## 検索


~~~py
In [1]: from products.indexers import *

In [2]: hit = ProductIndexer.search().query('match', description=u"テキパキ").execute().hits[0]

In [3]: hit.meta.to_dict()
Out[3]:
{'doc_type': u'products.product',
 u'id': u'3',
 u'index': u'django',
 u'score': 0.028767452}
~~~

モデル取得

~~~py
In [5]: ProductIndexer.from_hit(hit)
Out[5]: <Product: Trimming>
~~~
