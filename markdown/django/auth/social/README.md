- [#24](https://github.com/hdknr/annotated-django/issues/24)
- [Python Social Auth](https://python-social-auth.readthedocs.io/en/latest/#)
- [サンプル](python-social-auth.sample.md)
- [認証リクエストの流れ](psa.authreq.md)
- [認証応答のランディングの流れ](psa.authres.md)
- [Implicit Flowでのトークン受け渡し(DRF)](psa.implicit.md)

## facebook

- [FacebookログインとAccount Kit](https://developers.facebook.com/products/account-creation)

- [Facebook Backends](https://python-social-auth.readthedocs.io/en/latest/backends/facebook.html)
- [how to get user email with python social auth with facebook and save it](http://stackoverflow.com/questions/21968004/how-to-get-user-email-with-python-social-auth-with-facebook-and-save-it)

## アーキテクチャ

- `Webフレームワーク` と `認証プロバイダバックエンド` の組み合わせで動作するようになっている
- `Webフレームワークは `INSTALLED_APPS` に指定した python-social-authのアプリで決まる
- `認証プロバイダバックエンド` は url で決まる
- `認証プロバイダバックエンド` に `Webフレームワーク` ごとの `ストラテジ` をもたせて実際のロジックをストラテジに任せる
- `ストラテジ` を動作せせるために `パイプライン` に定義したタスクを逐次実行して、認証応答からログイン処理までを実行する
- データの保存を抽象化するために `Webフレームワーク` ごとに `ストレージ` が紐づけられる
- 認証要求/応答の処理は `アクション` に定義されていて、そこで `パイプライン` が実行される
- `パイプライン` の間に　UI を挟むことができるように `パーシャルパイプライン` で `パイプライン`を中断させて、UIがもどってから再開させることができる

- [Strategy (ストラテジ)](https://www.techscore.com/tech/DesignPattern/Strategy.html/)

- strategies/django_strategy.py

~~~py
class BaseStrategy(object):                                                         

    def create_user(self, *args, **kwargs):                                         
        '''
        - storage: 'social.apps.django_app.default.models.DjangoStorage'
        - user :  'social.apps.django_app.default.models.UserSocialAuth'
        '''
        return self.storage.user.create_user(*args, **kwargs)     
~~~        



## 記事

- [Djangoでスマホアプリ向けにソーシャル連携APIを作る](http://qiita.com/koyopro/items/f106d24c08ac0ec32494)
- [python-social-authを使用時，メールアドレスのドメインで認証可否を制御する](http://qiita.com/shiccocsan/items/adcead2eee09daa930fa)
