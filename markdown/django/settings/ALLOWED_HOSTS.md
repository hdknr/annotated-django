## nginx で設定する

local_settings.py:

~~~py
ALLOWED_HOSTS = ['shop.lafoglia.jp', 'localhost', ]
~~~

~~~
server {
    client_max_body_size 30M;
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    server_name _;

    # IPアドレスが指定されたらホスト名を書き換える
    # AWS LBS からIPアドレス指定でアクセスされるので。通常はブラウザがDNSでアクセスする。
    set $my_host $host;
    if ($host ~ "\d+\.\d+\.\d+\.\d+") {
      set $my_host "shop.lafoglia.jp";
    }

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $my_host;
        proxy_redirect off;
        proxy_pass http://127.0.0.1:8000/;
        break;
    }
    location /static {
        autoindex on;
        alias /home/system/projects/shop/web/static;
        break;
    }
}
~~~

## django で EC2のアドレスを取得して追加する

~~~py
# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    'yourdomain.tld',
    '.compute-1.amazonaws.com', # allows viewing of instances directly
]

import requests
EC2_PRIVATE_IP  =   None
try:
    EC2_PRIVATE_IP  =   requests.get('http://169.254.169.254/latest/meta-data/local-ipv4', timeout = 0.01).text
except requests.exceptions.RequestException:
    pass

if EC2_PRIVATE_IP:
    ALLOWED_HOSTS.append(EC2_PRIVATE_IP)
~~~    


# 記事

- http://stackoverflow.com/questions/27720254/django-allowed-hosts-with-elb-healthcheck
- http://serverfault.com/questions/680705/configure-nginx-to-only-allow-specified-hosts
- https://www.xormedia.com/django-allowed-hosts-and-amazon-elastic-load-balancer/k
