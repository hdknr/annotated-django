# logstrash

- [Installing Logstash | Logstash Reference [6.5] | Elastic](https://www.elastic.co/guide/en/logstash/current/installing-logstash.html)

~~~bash
$ wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
OK
~~~

~~~bash
$ sudo apt-get install apt-transport-https

パッケージリストを読み込んでいます... 完了
依存関係ツリーを作成しています                
状態情報を読み取っています... 完了
apt-transport-https はすでに最新バージョン (1.6.6) です。
アップグレード: 0 個、新規インストール: 0 個、削除: 0 個、保留: 3 個
~~~

~~~bash 
$ grep artifacts /etc/apt/sources.list.d/elastic-6.x.list | grep -v "^#"
# echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list

deb https://artifacts.elastic.co/packages/6.x/apt stable main
~~~

~~~bash 
$ sudo apt-get update && sudo apt-get install logstash
.
~~~

~~~bash
$ dpkg -L logstash | grep  "^/etc"

/etc
/etc/logstash
/etc/logstash/logstash.yml
/etc/logstash/logstash-sample.conf
/etc/logstash/startup.options
/etc/logstash/jvm.options
/etc/logstash/log4j2.properties
/etc/logstash/conf.d
/etc/logstash/pipelines.yml
~~~