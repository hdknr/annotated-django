SSL環境化でリバースプロキシで動く場合
--------------------------------------

nginx ngx_http_proxy_module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- `Module ngx_http_proxy_module <http://nginx.org/en/docs/http/ngx_http_proxy_module.html>`_

::

    location / {

      proxy_set_header        Host $host;
      proxy_set_header        X-Real-IP $remote_addr;
      proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header        X-Forwarded-Proto $scheme;

    }

apache mod_proxy
^^^^^^^^^^^^^^^^^^

- `Apache Module mod_proxy<https://httpd.apache.org/docs/2.4/en/mod/mod_proxy.html>`_
- `Apache Module mod_headers <https://httpd.apache.org/docs/current/en/mod/mod_headers.html>`_

::

    RequestHeader unset X-Forwarded-Proto
    RequestHeader set X-Forwarded-Proto https env=HTTPS


