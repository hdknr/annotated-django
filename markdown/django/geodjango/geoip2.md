# GeoIP2

- https://docs.djangoproject.com/ja/2.1/ref/contrib/gis/geoip2/

Ubuntu:

~~~bash 
$ sudo apt-get install libmaxminddb0 -y
~~~

[macOS](http://macappstore.org/libmaxminddb/):

~~~bash 
$ brew install libmaxminddb
~~~


## gioip2 

- https://geoip2.readthedocs.io/en/latest/

PIP:

~~~bash 
$ pip install geoip2 
~~~

## データ

~~~bash 
$ curl -L http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz | gunzip -c data/GeoLite2-City.mmdb
~~~

## settings.py

~~~py
GEOIP_PATH = os.path.join(BASE_DIR, 'data')
~~~

## 例:

~~~py
In [1]: from django.contrib.gis.geoip2 import GeoIP2
In [2]: g = GeoIP2()

In [3]: g.city('153.201.112.117')
Out[3]:
{'city': 'Fujisawa',
 'continent_code': 'AS',
 'continent_name': 'Asia',
 'country_code': 'JP',
 'country_name': 'Japan',
 'dma_code': None,
 'latitude': 35.3493,
 'longitude': 139.4767,
 'postal_code': '251-0052',
 'region': '14',
 'time_zone': 'Asia/Tokyo'}
~~~

## 言語

- [GeoIP2: 言語引数が指定できないのはなぜか?](https://github.com/hdknr/annotated-django/commit/57bfcad841fac5c23c324fd2cd6bede953f5c80b)
- `postal_code` で検索する? ([YOLP(地図):郵便番号検索API - Yahoo!デベロッパーネットワーク](https://developer.yahoo.co.jp/webapi/map/openlocalplatform/v1/zipcodesearch.html)
 )
- [郵便番号検索API - zipcloud](http://zipcloud.ibsnet.co.jp/doc/api)

## 記事

- [GeoLite2でサクッとできるIPアドレスの国判定 ｜ Developers.IO](https://dev.classmethod.jp/cloud/aws/geolite2-python/)
- [IPアドレスからそれっぽい位置情報を取得したい - パルカワ2](http://hisaichi5518.hatenablog.jp/entry/2014/08/18/172949)
