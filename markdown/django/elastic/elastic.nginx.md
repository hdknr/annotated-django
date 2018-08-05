## location

TCP9200 にリバースプロキシ:

~~~
location /es/ {
  if ($request_method != GET) {
    return 403;
  }
  proxy_pass http://127.0.0.1:9200/;
}
~~~