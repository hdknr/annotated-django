# インデックステンプレート

- [Index Templates | Elasticsearch Reference [6.5] | Elastic](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-templates.html)
- インデックスが作成されるタイミングで自動的に適用される設定をテンプレートとして登録できる機能
- 実際にテンプレートが適用されるかどうかは、インデックス名で判断

内容:

- [設定](https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules.html#index-modules-settings)
- [マッピング](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping.html)

## 例

~~~bash 
curl http://develop.local:9200/_template/test-blog | jq "."
~~~

~~~json
{
  "test-blog": {
    "order": 0,
    "index_patterns": [
      "test-blog-*"
    ],
    "settings": {
      "index": {
        "number_of_shards": "1",
        "number_of_replicas": "0"
      }
    },
    "mappings": {
      "doc": {
        "properties": {
          "title": {
            "type": "text"
          },
          "published": {
            "type": "date"
          },
          "tags": {
            "type": "keyword"
          },
          "content": {
            "type": "text"
          }
        }
      }
    },
    "aliases": {}
  }
}
~~~

## index_patterns

- 指定されたインデック名にテンプレートが適用される
- [Support regex or array template pattern match · Issue #20690 · elastic/elasticsearch](https://github.com/elastic/elasticsearch/issues/20690)
