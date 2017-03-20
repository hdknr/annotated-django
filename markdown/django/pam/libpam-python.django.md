staging環境に基本認証

- ID管理が面倒くさいのでDjango Userのクレデンシャルを使う
- nginxでPAM認証かけてlibpam-python からスクリプトを呼ぶ
- スクリプトのなかで `django.contrib.auth.authenticate`を検証する

## Ubuntuにパッケージインストール

~~~bash
$ sudo apt-get install -y libpam-python python-pip libmysqlclient-dev
~~~

~~~bash
$ dpkg -L libpam-python | grep so
/lib/x86_64-linux-gnu/security/pam_python.so

$ sudo which pip
/usr/bin/pip
~~~

~~~bash
$ sudo pip install django MySQL-python
~~~


## nginx

~~~bash
$ sudo nginx -V  2>&1 |  sed 's/--/\n--/g' | grep pam | wc
      0       0       0
~~~

~~~bash
$ sudo apt-get install nginx-full
~~~
~~~bash
$ sudo nginx -V  2>&1 |  sed 's/--/\n--/g' | grep pam
--add-module=/build/nginx-pzhfc2/nginx-1.10.0/debian/modules/nginx-auth-pam
~~~

## 認証スクリプト

/home/admin/projects/mysite/web/app/pamauth.py:

~~~py
# settings.py より SECRET_KEY, DATABASESをコピー
SECRET_KEY = '{{ シークレット}}'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'NAME': 'apps_alpha',
        'USER': 'apps_alpha',
        'PASSWORD': 'apps_alpha',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    },
}
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
]
####

# pip install django MySQL-python

import syslog
import sys
import traceback
#

NAME = 'pamauth'

syslog.openlog(ident=NAME,
               logoption=syslog.LOG_PID, facility=syslog.LOG_LOCAL0)

def configure():
    from django import setup
    from django.conf import settings

    settings.configure(
        SECRET_KEY=SECRET_KEY,
        DATABASES=DATABASES,
        INSTALLED_APPS=INSTALLED_APPS,
    )
    setup()

try:
    configure()
except:
    print traceback.format_exc()
    pass


def pam_sm_authenticate(pamh, flags, argv):
    syslog.syslog("%s: flag = %s" % (NAME, str(flags)))
    syslog.syslog("%s: argv= %s" % (NAME, str(argv)))

    if pamh.authtok is None:
        passmsg = pamh.Message(pamh.PAM_PROMPT_ECHO_OFF,
                               "Authenticate: password?")
        res = pamh.conversation(passmsg)
        syslog.syslog("%s:response is %s" % (NAME, res.resp))
        pamh.authtok = res.resp

    auth_class = argv[1] if len(argv) > 1 else None

    username = pamh.user
    password = pamh.authtok

    # syslog.syslog("%s: user= %s" % (NAME, username))
    # syslog.syslog("%s: service= %s" % (NAME, pamh.service))
    # syslog.syslog("%s: password = %s" % (NAME, password))
    # syslog.syslog("%s: rhost = %s" % (NAME, pamh.rhost))

    try:
        if authenticate(username, password,
                        pamh and pamh.service, auth_class):
            syslog.syslog("%s: Authenticated !!! " % NAME)
            return pamh.PAM_SUCCESS
    except:
        for err in traceback.format_exc().split('\n'):
            syslog.syslog("%s: %s" % (NAME, err))

    return pamh.PAM_AUTH_ERR


def authenticate(username, password, service=None, auth_class=None):
    ''' Django で認証させる '''
    from django.contrib.auth import authenticate
    user = authenticate(username=username, password=password)

    return True if user else False


def pam_sm_setcred(pamh, flags, argv):
    syslog.syslog("ANY_AUTH:pam_sm_setcred")
    return pamh.PAM_CRED_ERR


def pam_sm_acct_mgmt(pamh, flags, argv):
    syslog.syslog("ANY_AUTH:pam_sm_acct_mgmt")
    return pamh.PAM_SUCCESS


def pam_sm_open_session(pamh, flags, argv):
    syslog.syslog("ANY_AUTH:pam_sm_open_session")
    return pamh.PAM_SUCCESS


def pam_sm_close_session(pamh, flags, argv):
    syslog.syslog("ANY_AUTH:pam_sm_close_session")
    return pamh.PAM_SUCCESS


def pam_sm_chauthtok(pamh, flags, argv):
    syslog.syslog("ANY_AUTH:pam_sm_chauthtok")
    return pamh.PAM_SUCCESS


if __name__ == '__main__':
    if len(sys.argv) > 2:
        print "Authcatiion for %s %s" % (sys.argv[1], sys.argv[2]),
        print ":", authenticate(*sys.argv[1:])
~~~        

## PAM 設定

~~~bash
$ sudo vi /etc/pam.d/nginx-basicauth
~~~

~~~
auth    sufficient      pam_python.so   /home/admin/projects/mysite/web/app/pamauth.py
account required        pam_permit.so
~~~

## nginx 設定

/etc/nginx/sites-available/basicauth.conf :

~~~
auth_pam "Django User Auth";                  # RELMの設定
auth_pam_service_name "nginx-basicauth";      # PAMの設定
~~~

/etc/nginx/sites-available/default:

~~~
location / {
    include /etc/nginx/sites-available/basicauth.conf ;
    include /etc/nginx/sites-available/app.conf ;
}
~~~
