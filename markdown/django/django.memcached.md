- [DjangoによるMemcached設定](http://qiita.com/pollseed/items/154303e9b539e6b245a2)
- [Start using memcache](https://devcenter.heroku.com/articles/django-memcache#start-using-memcache)
- [django-pylibmc/django-pylibmc](https://github.com/django-pylibmc/django-pylibmc)
- [akshayohri/django-pylibmc-python3](https://github.com/akshayohri/django-pylibmc-python3)
- [pylibmc](http://sendapatch.se/projects/pylibmc/#)
- [linsomniac/python-memcached](https://github.com/linsomniac/python-memcached)
- [eguven/python3-memcached](https://github.com/eguven/python3-memcached)
- [libmemcached-tools](https://packages.debian.org/sid/utils/libmemcached-tools)

# Memcached

- Debian

~~~bash
$ sudo apt-get install memcached libmemcached-dev libmemcached-tools -y

$ ps axu | grep "^mem"

memcache  6967  0.0  0.1 327452  2648 ?        
  Ssl  03:41   0:00 /usr/bin/memcached -m 64 -p 11211 -u memcache -l 127.0.0.1

$ sudo lsof -i:11211

COMMAND    PID     USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
memcached 6967 memcache   26u  IPv4 568045      0t0  TCP localhost:11211 (LISTEN)  
~~~

- フラッシュ

~~~py
import memcache                          
mc = memcache.Client(['localhost:11211'])
mc.flush_all()
~~~

- [すべてのキー](http://www.darkcoding.net/software/memcached-list-all-keys/)

~~~bash
$ telnet 127.0.0.1 11211
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
stats items
STAT items:4:number 1
...
STAT items:30:number 1
...
END
~~~

- [get all keys set in memcached](http://stackoverflow.com/questions/19560150/get-all-keys-set-in-memcached)

# Django キャッシュ

- [Django’s cache framework](https://docs.djangoproject.com/ja/2.1/topics/cache/#django-s-cache-framework)

どちらか:

~~~bash
$ pip install python-memcached
$ pip install pylibmc
~~~

python-memcached:

~~~py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
~~~

pylibmc:

~~~py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
~~~

## 基本操作

30秒間キャッシュさせる:

~~~py
In [1]: from django.core.cache import cache

In [2]: cache.set('my_key', 'hello, world!', 30)

In [3]: cache.get('my_key')
Out[3]: 'hello, world!'

In [4]: cache.get('my_key')
None
~~~

インクリメント:

~~~py
In [4]: cache.set('num', 1)

In [5]: cache.incr('num')
Out[5]: 2

In [6]: cache.decr('num')
Out[6]: 1
~~~

削除:

~~~py
In [7]: cache.delete('num')
~~~

## バックエンド

バックエンド:

- [Memcached](https://docs.djangoproject.com/en/dev/topics/cache/#memcached)
- [データベースキャッシュ](https://docs.djangoproject.com/en/dev/topics/cache/#database-caching)
- [ファイルキャッシュ](https://docs.djangoproject.com/en/dev/topics/cache/#filesystem-caching)
- [メモリキャッシュ](https://docs.djangoproject.com/en/dev/topics/cache/#local-memory-caching)
- [開発用のダミーキャッシュ](https://docs.djangoproject.com/en/dev/topics/cache/#dummy-caching-for-development)
- [カスタムキャッシュ](https://docs.djangoproject.com/en/dev/topics/cache/#using-a-custom-cache-backend)

パラメータ

- [キャッシュ引数](https://docs.djangoproject.com/en/dev/topics/cache/#cache-arguments)

## キャッシュの利用

- [サイト](https://docs.djangoproject.com/en/dev/topics/cache/#the-per-site-cache)
- [ビュー](https://docs.djangoproject.com/en/dev/topics/cache/#the-per-view-cache)
- [テンプレート](https://docs.djangoproject.com/en/dev/topics/cache/#template-fragment-caching)


- [キャッシュキーは WSGIRequestを使って決められる](https://github.com/hdknr/annotated-django/commit/d66b4c03cfc2078ff2f28103734f74e846084409)

~~~bash
$ memcdump --servers=localhost:11211
:1:views.decorators.cache.cache_header..9345faba5ae09e1bd9a1200c63dfd976.ja.Asia/Tokyo
:1:views.decorators.cache.cache_page..GET.9345faba5ae09e1bd9a1200c63dfd976.d41d8cd98f00b204e9800998ecf8427e.ja.Asia/Tokyo
~~~

## API

- [参照](https://docs.djangoproject.com/en/dev/topics/cache/#the-low-level-cache-api)
- [キーのプレフィックス](https://docs.djangoproject.com/en/dev/topics/cache/#cache-key-prefixing)
- [キャッシュバージョン](https://docs.djangoproject.com/en/dev/topics/cache/#cache-versioning)
- [キーの変更](https://docs.djangoproject.com/en/dev/topics/cache/#cache-key-transformation)
- [キーの警告](https://docs.djangoproject.com/en/dev/topics/cache/#cache-key-warnings)


## ダウンストリーム

- [Varyヘッダー](https://docs.djangoproject.com/en/dev/topics/cache/#using-vary-headers)
- [キャッシュコントロール](https://docs.djangoproject.com/en/dev/topics/cache/#controlling-cache-using-other-headers)
