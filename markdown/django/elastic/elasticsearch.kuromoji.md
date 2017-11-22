
## kuromoji プラグイン

- [Japanese (kuromoji) Analysis Plugin](https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-kuromoji.html)
- [Haystack + Elasticsearch + kuromoji コトハジメ](https://gist.github.com/voluntas/6739918)
- [Elasticsearch に kuromoji を入れて日本語全文検索をする](http://qiita.com/mserizawa/items/8335d39cacb87f12b678)
- [Elasticsearchとkuromojiでちゃんとした日本語全文検索をやるメモ](http://tech.gmo-media.jp/post/70245090007/elasticsearch-kuromoji-japanese-fulltext-search)

~~~bash
$ sudo /usr/share/elasticsearch/bin/plugin install analysis-kuromoji

-> Installing analysis-kuromoji...
Trying https://download.elastic.co/elasticsearch/release/org/elasticsearch/plugin/analysis-kuromoji/2.3.2/analysis-kuromoji-2.3.2.zip ...
Downloading ............DONE
Verifying https://download.elastic.co/elasticsearch/release/org/elasticsearch/plugin/analysis-kuromoji/2.3.2/analysis-kuromoji-2.3.2.zip checksums if available ...
Downloading .DONE
Installed analysis-kuromoji into /usr/share/elasticsearch/plugins/analysis-kuromoji
~~~

~~~bash
$ sudo /etc/init.d/elasticsearch restart
~~~

~~~bash
$ curl -X GET 'http://localhost:9200/_nodes/plugins' | jq ".nodes[].plugins[]"
~~~

~~~javascript
{
  "name": "analysis-kuromoji",
  "version": "2.3.2",
  "description": "The Japanese (kuromoji) Analysis plugin integrates Lucene kuromoji analysis module into elasticsearch.",
  "jvm": true,
  "classname": "org.elasticsearch.plugin.analysis.kuromoji.AnalysisKuromojiPlugin",
  "isolated": true,
  "site": false
}
{
  "name": "head",
  "version": "master",
  "description": "head - A web front end for an elastic search cluster",
  "url": "/_plugin/head/",
  "jvm": false,
  "site": true
}
~~~

~~~bash
$ sudo vi /etc/elasticsearch/elasticsearch.yml

$ sudo tail  /etc/elasticsearch/elasticsearch.yml

# ########
# Kuromoji
index.analysis.analyzer.default.type: custom
index.analysis.analyzer.default.tokenizer: kuromoji_tokenizer

~~~

~~~bash
$ sudo /etc/init.d/elasticsearch restart
[ ok ] Restarting elasticsearch (via systemctl): elasticsearch.service.
~~~

- データ投入

~~~bash
$ curl -X POST http://localhost:9200/wine/sample/_bulk --data-binary @wine.json  
~~~

- クエリ

~~~bash
$ curl -X GET http://localhost:9200/wine/sample/_search -d '{"query":{"match":{"description":"渋め"}}}'
~~~
