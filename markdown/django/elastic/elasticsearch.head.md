# elasticsearch-head

- A web front end for an elastic search cluster http://mobz.github.io/elasticsearch-head/
- https://github.com/mobz/elasticsearch-head

~~~bash
$ git clone git://github.com/mobz/elasticsearch-head.git
$ cd elasticsearch-head
$ npm install
$ npm run start
...
~~~

~~~bash
> elasticsearch-head@0.0.0 start /vagrant/projects/taberutabi/elasticsearch-head
> grunt server

(node:4581) ExperimentalWarning: The http2 module is an experimental API.
Running "connect:server" (connect) task
Waiting forever...
Started connect web server on http://localhost:9100
~~~

develop.local サーバー:

~~~bash
$ curl -I http://develop.local:9100
.
~~~

~~~bash
HTTP/1.1 200 OK
Accept-Ranges: bytes
Cache-Control: public, max-age=0
Last-Modified: Tue, 08 Jan 2019 07:52:45 GMT
ETag: W/"446-1682c731325"
Content-Type: text/html; charset=UTF-8
Content-Length: 1094
Date: Tue, 08 Jan 2019 07:57:49 GMT
Connection: keep-alive
~~~

## `cluster health: not connected`

~~~bash
$ sudo vim /etc/elasticsearch/elasticsearch.yml
..
~~~

~~~yaml
http.cors.enabled: true
http.cors.allow-origin: "*"
~~~

~~~bash
$ sudo /etc/init.d/elasticsearch restart

[ ok ] Restarting elasticsearch (via systemctl): elasticsearch.service.
~~~
