# Elasticsearch

- https://www.elastic.co/

## インストール

- [Repositories](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-repositories.html)

### Debian Jessie

- [Install Elasticsearch with Debian Package](https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html#deb)


~~~bash
$ wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

OK

$ sudo apt-get install apt-transport-https

$ echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list
~~~


~~~bash
$ sudo apt-get install apt-transport-https
$ sudo apt-get update
$ sudo apt-get install elasticsearch
~~~

#### Java

- [Easy install for elasticsearch on Ubuntu 14.04](https://gist.github.com/Globegitter/662713f90d5af5b4269d)
- [How to install OpenJDK 8 on 14.04 LTS?](http://askubuntu.com/questions/464755/how-to-install-openjdk-8-on-14-04-lts)

~~~bash
$ sudo apt-get install openjdk-8-jre-headless -y
~~~

#### 起動:SysVInit

~~~bash
$ sudo update-rc.d elasticsearch defaults 95 10
~~~

~~~bash
$ sudo /etc/init.d/elasticsearch restart
[ ok ] Restarting elasticsearch (via systemctl): elasticsearch.service.
~~~

~~~bash
$ sudo lsof -u elasticsearch | grep TCP

java    2293 elasticsearch  114u     IPv6             351351      0t0     TCP localhost:9300 (LISTEN)
java    2293 elasticsearch  116u     IPv6             351361      0t0     TCP localhost:9300 (LISTEN)
java    2293 elasticsearch  123u     IPv6             351410      0t0     TCP localhost:9200 (LISTEN)
java    2293 elasticsearch  124u     IPv6             351411      0t0     TCP localhost:9200 (LISTEN)
~~~

~~~bash
$ curl -XGET http://localhost:9200/

{
  "name" : "OSPJ8d_",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "qCA9JNPwTWS3coNUinHI3g",
  "version" : {
    "number" : "6.0.0",
    "build_hash" : "8f0685b",
    "build_date" : "2017-11-10T18:41:22.859Z",
    "build_snapshot" : false,
    "lucene_version" : "7.0.1",
    "minimum_wire_compatibility_version" : "5.6.0",
    "minimum_index_compatibility_version" : "5.0.0"
  },
  "tagline" : "You Know, for Search"
}
~~~

## 0.0.0.0 にバインドさせる(開発環境)

- [基本設定](http://sebrain.web.fc2.com/document/0064.html)

~~~bash
$ grep ^network /etc/elasticsearch/elasticsearch.yml

network.host: 0.0.0.0
~~~

~~~bash
$ sudo lsof -u elasticsearch | grep TCP
java    2599 elasticsearch  114u     IPv6             352313      0t0     TCP *:9300 (LISTEN)
java    2599 elasticsearch  122u     IPv6             352357      0t0     TCP *:9200 (LISTEN)
~~~



## python / Django

- [Django から Elasticsearch を使う](http://qiita.com/Fq4X/items/81ba2f234e9611546025)
- [Django + Haystack + Elasticsearch コトハジ](https://gist.github.com/voluntas/21759d5c45aacc0e6656/)
- [pythonクライアントで始める「はじめてのElasticsearch」](http://qiita.com/ikawaha/items/c654f746cfe76b888a27)

### PYPI elasticsearch :Python Elasticsearch Client

- https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/index.html
- https://pypi.python.org/pypi/elasticsearch/2.3.0
- http://elasticsearch-py.readthedocs.io/en/master/

~~~bash
$ pip install elasticsearch
~~~

~~~python
In [1]: from elasticsearch import Elasticsearch
In [2]: es = Elasticsearch("localhost:9200")
In [4]: es
Out[4]: <Elasticsearch([{u'host': u'localhost', u'port': 9200}])>
In [5]: res = es.search(index='wine', body={"query": {"match":{"description":"渋め"}}})
In [8]: for hit in res['hits']['hits']:
   ...:     print hit['_source']['name']
   ...:     
カベルネ・ソーヴィニヨン
ピノ・ノワール
~~~

# AWS

- [Amazon Elasticsearch Service](https://aws.amazon.com/jp/elasticsearch-service/)
- [Amazon Elasticsearch Serviceでkuromojiを使って日本語全文検索する](http://dev.classmethod.jp/cloud/aws/using-kuromoji-on-amazon-es/)

- Amazon ESとしてはプラグインの追加機能が提供されていないため、最初からKuromojiが含まれているのは、日本においてはすごく重要です。


## その他

- [Elastic Searchで全てのデータ(index)を削除する](http://qiita.com/shouta-dev/items/c2d2eb6cf61bb1fa8e1b)

~~~bash
$ curl -XDELETE 'http://localhost:9200/*'
{"acknowledged":true}
~~~
