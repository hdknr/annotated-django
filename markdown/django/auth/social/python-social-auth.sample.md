
- [Python Social Auth](https://python-social-auth.readthedocs.io/en/latest/#)

#  Facebookでログインさせるまで

## インストール

~~~py
$ pip install python-social-auth
~~~

## settings.py

~~~py
TEEMPLATES = [
     {
         ....
         'OPTIONS': {
             'context_processors': [
                ...
                # 追加
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
             ],
         },
     },
 ]
~~~

~~~py
INSTALLED_APPS = [
  ....
  social.apps.django_app.default',       # pytho-social-auth
]
~~~

~~~py
from django.conf import global_settings
AUTHENTICATION_BACKENDS = [
     'social.backends.facebook.FacebookOAuth2',   # とりあえずFacebook
] + global_settings.AUTHENTICATION_BACKENDS
~~~

~~~py
SOCIAL_AUTH_PIPELINE = [
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
]
~~~

## マイグレーション

~~~py
$ python manage.py migrate

Running migrations:
  Applying social_auth.0001_initial... OK
  Applying social_auth.0002_add_related_name... OK
  Applying social_auth.0003_alter_email_max_length... OK
  Applying social_auth.0004_auto_20160423_0400... OK
  Applying social_auth.0005_auto_20160727_2333... OK
~~~

## urls.py

- '/accounts/social' のパスにしたいので

accounts/urls.py:

~~~py
from django.conf.urls import url, include

urlpatterns = [
    ...
    url('^social/', include('social.apps.django_app.urls', namespace='social')),
    ...
]
~~~

- 確認

~~~py
In [1]: from django.core.urlresolvers import reverse

In [2]: reverse('social:begin', kwargs={'backend': 'facebook'})
Out[2]: u'/accounts/social/login/facebook/'
~~~

## ログインボタン

accounts/auth/login.html:

~~~py
<a class="btn btn-primary"
  href="{% url 'social:begin' backend='facebook'  %}">
    {% trans 'Facebook Login' %}</a>
~~~

## Facebook にアプリ登録

- http://developers.facebook.com/setup/
- ``有効なOAuthリダイレクトURI`:  http://localhost:8000/accounts/social/complete/facebook/

settings.py:

~~~py
SOCIAL_AUTH_FACEBOOK_KEY = "9766949723637785"
SOCIAL_AUTH_FACEBOOK_SECRET = "3d80cf3be0662d07f773cbd7e3f77237"
~~~


# メールアドレスをユーザー名にする

- settings.py

~~~py
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email',
}
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
~~~

~~~py
SOCIAL_AUTH_PIPELINE = [
    ...
    'social.pipeline.user.get_username',      # 追加
    'social.pipeline.user.create_user',
    ...
]
~~~

# ユーザー作成後にグループ追加などをする(パイプラインカスタマイズ)

accounts/pipline.py:

~~~py
from social.pipeline.user import create_user as psa_create_user

def provice_user(user):
  # グループ追加とかパーミッション追加とか
  pass


def create_user(strategy, details, user=None, *args, **kwargs):
    from members.models import Member
    res = psa_create_user(
        strategy, details, user=user, *args, **kwargs)

    created = res.get('user', None)
    if created:
        provide_user(created)       
    return res
~~~

settings.py:

~~~py
SOCIAL_AUTH_PIPELINE = [
    ...
    'social.pipeline.user.get_username',      
    'accounts.pipeline.create_user',        # カスタマイズしたパイプライン
    ...
]
~~~
