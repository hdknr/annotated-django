
- [Session](https://docs.djangoproject.com/en/1.9/topics/http/sessions/)
- [How to expire Django session in 5minutes?](http://stackoverflow.com/questions/14830669/how-to-expire-django-session-in-5minutes)

# 設定

## SESSION_COOKIE_AGE

- セッション保持秒数
- [Settings](https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-SESSION_COOKIE_AGE)

~~~py
In [4]: settings.SESSION_COOKIE_AGE
Out[4]: 1209600
~~~

## SESSION_EXPIRE_AT_BROWSER_CLOSE

- [django 1.8 SESSION_EXPIRE_AT_BROWSER_CLOSE not working](http://stackoverflow.com/questions/30093624/django-1-8-session-expire-at-browser-close-not-working)
- [Browser-length sessions vs. persistent sessions](https://docs.djangoproject.com/en/1.9/topics/http/sessions/#browser-length-sessions-vs-persistent-sessions)


- デフォルト = False (SESSION_COOKIE_AGE でタイムアウト)

~~~py
In [2]: from django.conf import settings
In [3]: settings.SESSION_EXPIRE_AT_BROWSER_CLOSE
Out[3]: False
~~~



# セッションエンジン

~~~
>>> from django.conf import settings
>>> settings.SESSION_ENGINE
'django.contrib.sessions.backends.db'
>>> engine = __import__(settings.SESSION_ENGINE, {}, {}, [''])
>>> dir()
['__builtins__', 'engine', 'settings']
~~~

## エンジンからセッションのロード

```
>>> engine.SessionStore(u'qzoehydb7vsxp7s3ipc5b92y95ah0rhs')
<django.contrib.sessions.backends.db.SessionStore object at 0x7fefb7896590>
>>> sobj = _
```

```
>>> sobj.keys()
[u'_auth_user_hash', u'_auth_user_id', u'_auth_user_backend']

>>> sobj['_auth_user_id']
1
```

```
>>> sobj['password_expired'] = True
>>> sobj.save()
```

# セッションストア

~~~py
In [1]: from django.contrib.sessions.models import Session
In [2]: ses = Session.objects.first()

In [3]: ses.get_session_store_class()
Out[3]: django.contrib.sessions.backends.db.SessionStore
In [5]: store = ses.get_session_store_class()()

In [6]: store
Out[6]: <django.contrib.sessions.backends.db.SessionStore at 0x7f917e250080>
In [7]: store.decode(ses.session_data)
Out[7]:
{'_auth_user_backend': 'django.contrib.auth.backends.ModelBackend',
 '_auth_user_hash': 'ee68be6809680dcd1e2a3aee80d0d7fc0e5abc08',
 '_auth_user_id': '1'}

In [8]: ses.get_decoded()
Out[8]:
{'_auth_user_backend': 'django.contrib.auth.backends.ModelBackend',
 '_auth_user_hash': 'ee68be6809680dcd1e2a3aee80d0d7fc0e5abc08',
 '_auth_user_id': '1'
>>> type(_)
<type 'dict'>
~~~

## セッションハッシュの検証


~~~py
In [9]: sessionid = 'bgbwo7e5hckvsq4191o9k0dptcbvdiyx'

In [10]: Session._meta.fields
Out[10]:
(<django.db.models.fields.CharField: session_key>,
 <django.db.models.fields.TextField: session_data>,
 <django.db.models.fields.DateTimeField: expire_date>)

In [11]: ses = Session.objects.filter(session_key=sessionid).first()
In [12]: ses
Out[12]: <Session: bgbwo7e5hckvsq4191o9k0dptcbvdiyx>

In [13]: ses.session_data
Out[13]: 'MTJlMGUyOTEwNDhkNWE5MjgyY2Q5MTQ0MjRhODkwZmU3ODZiNmJiODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlZTY4YmU2ODA5NjgwZGNkMWUyYTNhZWU4MGQwZDdmYzBlNWFiYzA4In0='

In [14]: import base64

In [15]: encoded_data = base64.b64decode(ses.session_data)

In [16]: encoded_data
Out[16]: b'12e0e291048d5a9282cd914424a890fe786b6bb8:{"_auth_user_id":"1","_auth_user_backend":"django.contrib.auth.backends.ModelBackend","_auth_user_hash":"ee68be6809680dcd1e2a3aee80d0d7fc0e5abc08"}'

In [18]: hash, serialized = encoded_data.split(b':', 1)

In [19]: hash
Out[19]: b'12e0e291048d5a9282cd914424a890fe786b6bb8'

In [20]: serialized
Out[20]: b'{"_auth_user_id":"1","_auth_user_backend":"django.contrib.auth.backends.ModelBackend","_auth_user_hash":"ee68be6809680dcd1e2a3aee80d0d7fc0e5abc08"}'


In [21]: hash.decode()
Out[21]: '12e0e291048d5a9282cd914424a890fe786b6bb8'


In [22]: from django.utils.crypto import salted_hmac
In [23]: from django.contrib.sessions.backends.db import SessionStore

In [25]: SessionStore.__name__
Out[25]: 'SessionStore'

In [26]: key_salt = "django.contrib.sessions" + SessionStore.__name__
In [27]: key_salt
Out[27]: 'django.contrib.sessionsSessionStore'

In [28]: salted_hmac(key_salt, serialized)
Out[28]: <hmac.HMAC at 0x7f917d72eb38>

In [29]: _.hexdigest()
Out[29]: '12e0e291048d5a9282cd914424a890fe786b6bb8'

In [30]: _ == hash.decode()
Out[30]: True


~~~


## セッションオブジェクトでデータを修正して保存

~~~
>>> sobj['password_expired'] = False
>>> sobj.save()
>>> Session.objects.all()[0].get_decoded()['password_expired']
False
~~~
