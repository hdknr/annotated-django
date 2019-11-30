# User-Agent

- [UserAgentからOS/ブラウザなどの調べかたのまとめ](http://qiita.com/nightyknite/items/b2590a69f2e0135756dc)

## Python

ua-parserを使う:

- [tobie/ua-parser: A multi-language port of Browserscope's user agent parser.](https://github.com/tobie/ua-parser)
- [ua-parser/uap-python: Python implementation of ua-parser](https://github.com/ua-parser/uap-python)

その他:

- [woothee/woothee-python: Woothee python implementation](https://github.com/woothee/woothee-python)
- [selwin/python-user-agents: A Python library that provides an easy way to identify devices like mobile phones, tablets and their capabilities by parsing (browser) user agent strings.](https://github.com/selwin/python-user-agents)
- [selwin/django-user_agents: A django package that allows easy identification of visitor's browser, OS and device information, including whether the visitor uses a mobile phone, tablet or a touch capable device.](https://github.com/selwin/django-user_agents)


## Edge

- [User-agent string changes (Windows) | Microsoft Docs](https://docs.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/compatibility/hh869301(v=vs.85))


Desktop:

~~~
Mozilla/5.0 (Windows NT 10.0; <64-bit tags>) AppleWebKit/<WebKit Rev> (KHTML, like Gecko) Chrome/<Chrome Rev> Safari/<WebKit Rev> Edge/<EdgeHTML Rev>.<Windows Build>
~~~

Mobile:

~~~
Mozilla/5.0 (WM 10.0; Android <Android Version>; <Device Manufacturer>; <Device Model>) AppleWebKit/<WebKit Rev> (KHTML, like Gecko) Chrome/<Chrome Rev> Mobile Safari/<WebKit Rev> Edge/<EdgeHTML Rev>.<Windows Build>
~~~

~~~py
In [33]: a = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240'
In [44]: re.search(r'\s+(?P<family>Edg\D+)/(?P<major>\d+)\.(?P<minor>\d+)', a).groupdict()
Out[44]: {'family': 'Edge', 'major': '12', 'minor': '10240'}
~~~

- [Edge のユーザーエージェントがいろいろとひどい - Qiita](https://qiita.com/Tzalik/items/980316d11c55acecbfa5)
- [Microsoft Edgeのユーザーエージェントがカオスなので注意 - Qiita](https://qiita.com/tonkotsuboy_com/items/7b36bdfc3a9a0970d23b)
- [IE (Internet Explorer) 11 は Trident/7. で判別するユーザエージェントから MSIE が消えた IE 11 の判別方法 | かきしちカンパニー Web Magazine](http://www.webmagazine.kakisiti.co.jp/?p=262)

~~~
IE 11	Trident/7.
IE 10	Trident/6.
IE 9	Trident/5.
IE 8	Trident/4.
~~~
