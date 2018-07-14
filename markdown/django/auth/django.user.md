## パスワードログイン


- [authenteicate](https://docs.djangoproject.com/en/2.0/_modules/django/contrib/auth/#authenticate) でバックエンドから `User` を見つける
- [login](https://docs.djangoproject.com/en/2.0/_modules/django/contrib/auth/#login) で見つかったユーザーをセッションに紐づける

~~~py
from django.contrib.auth import authenticate, login

user = authenticate(
    username=form.cleaned_data['username'], 
    password=form.cleaned_data['password']):

if user:
    login(request, user)
~~~


## 氏名

- `user.get_full_name()`


## 新規登録

- [エラーメッセージなど](https://github.com/hdknr/annotated-django/commit/0f4dad8ad61bc549aa7fa010961d36b5d11a9700)
