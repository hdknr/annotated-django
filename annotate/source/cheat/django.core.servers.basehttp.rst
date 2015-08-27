BaseHTTPServer
^^^^^^^^^^^^^^^^^^

- wsgirefの元になっているモジュール
- `BaseHTTPServer — Basic HTTP server <https://docs.python.org/2.7/library/basehttpserver.html#module-BaseHTTPServer>`_

WSGI
^^^^^^^^^^^^^^^^^^

- `wsgiref 0.1.2 <https://pypi.python.org/pypi/wsgiref>`_
- `cpython/Lib/wsgiref/simple_server.py <https://github.com/python/cpython/blob/2.7/Lib/wsgiref/simple_server.py>`_
- `The WSGI Reference Library <http://peak.telecommunity.com/wsgiref_docs/>`_

.. py:method:: wsgiref.simple_server.WSGIRequestHandler.get_environ

- 環境変数は  `HTTP_` が先頭に付けられて保存される
