# Wordpress

## PHP

- https://github.com/ruflin/Elastica

## 記事

- [Index JSON files in elasticsearch using Python? - Stack Overflow](https://stackoverflow.com/questions/43981275/index-json-files-in-elasticsearch-using-python)

~~~py
from elasticsearch import Elasticsearch, helpers
import sys, json

es = Elasticsearch()

def load_json(directory):
    " Use a generator, no need to load all in memory"
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(filename,'r') as open_file:
                yield json.load(open_file)

helpers.bulk(es, load_json(sys.argv[1]), index='my-index', doc_type='my-type')
~~~

- [How to configure ElasticSearch on WordPress](https://www.cloudways.com/blog/elasticsearch-on-wordpress/)
