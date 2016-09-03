パスワードリセットのカスタマイズサンプル

## 準備

- Django の `auth` のビューをコールする

~~~py
from django.contrib.auth import views as auth_views
~~~

- get_users をカスタマイズしたいので、フォームをカスタマイズ

~~~py
from . import forms
~~~

## views.py のパイプライン実装

~~~py
class PasswordResetView(core_views.View):
    @core_views.handler(
        url=r'^password/reset',
        name="accounts_password_reset", order=40,)
    def begin(self, request):
        ''' #1. リセットフォームを表示し、メールアドレスをPOSTバックさせて
                URLを添付したメールを送る
        '''
        try:
            return auth_views.password_reset(
                request,
                template_name='accounts/password/reset_begin.html',
                email_template_name='accounts/password/reset_email.txt',
                subject_template_name='accounts/password/reset_subject.txt',
                password_reset_form=forms.PasswordResetForm,    # Custom Form
                # token_generator=default_token_generator,
                post_reset_redirect='accounts_password_reset_accepted',
                from_email=config.PASSWORDRESET_MAIL_FROM,
                # extra_context=None,
                # html_email_template_name=None,
                extra_email_context={'request': request},
            )
        except Exception, ex:
            return self.render(
                'accounts/password/reset_error.html', ex=ex)

    @core_views.handler(
        url=r'^password/reset/accepted',
        name="accounts_password_reset_accepted", order=30,)
    def accepted(self, request):
        ''' #2. メール送信後に受け付け完了を表示する
        '''
        return auth_views.password_reset_done(
            request,
            template_name='accounts/password/reset_accepted.html',
            extra_context=None)

    # base64 されたUser.id
    UIDB64 = r'/(?P<uidb64>[0-9A-Za-z_\-]+)'
    # トークン
    TOKEN = r'/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$'      # NOQA

    @core_views.handler(
        url=r'^password/reset/confirm' + UIDB64 + TOKEN,
        name="accounts_password_reset_confirm", order=20,)
    def confirm(self, request, uidb64, token):
        ''' #3. メールに添付されたURLでリクエストしてきたら、パスワード変更をPOSTバック
            　　 させてOKだったらパスワード変更して、完了画面へリダイレクト
        '''
        return auth_views.password_reset_confirm(
            request, uidb64=uidb64, token=token,
            template_name='accounts/password/reset_confirm.html',
            # token_generator=default_token_generator,
            # set_password_form=SetPasswordForm,
            post_reset_redirect='accounts_password_reset_complete',
            extra_context=None)

    @core_views.handler(
        url=r'^password/reset/complete',
        name="accounts_password_reset_complete", order=20,)
    def complete(self, request):
        ''' #4. パスワードの変更が正しく行われた通知画面 '''
        return auth_views.password_reset_complete(
            request,
            template_name='accounts/password/reset_complete.html',
            extra_context=None)
~~~

## forms.PasswordResetForm の実装

- メールアドレスでのUserの特定に関して特殊なことをしている
- パスワードリセット要求をログに記録する

~~~py
from django.contrib.auth.forms import PasswordResetForm as DjPasswordResetForm
from . import models

class PasswordResetForm(DjPasswordResetForm):

    def get_users(self, email):
        '''(override) : Profileで特殊なことをしている
        (存在しなかったら条件を満たすユーザーを作成)
        '''
        profile = models.Profile.objects.get_or_provide(email=email)
        user = profile and profile.user \
            or User.objects.filter(email=email).first()
        if not user:
            raise Exception(_('No User was found for {}').format(email))
        return [user]

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        '''(override): パスワードリセットをLog に記録する
        '''
        if 'request' in context:
            try:
                # メールアドレス(to_email)と request.META を YAML で記録
                data = BaseObjectSerializer.to_yaml(
                    [{'to_email': to_email}, context['request'].META], indent=2)
                models.Log.objects.create(name=_('Password Reset'), data=data)
            except:
                logger.error(traceback.format_exc())

        super(PasswordResetForm, self).send_mail(
            subject_template_name, email_template_name,
            context, from_email, to_email,
            html_email_template_name=html_email_template_name)
~~~            

## オブジェクトをテキストに変換して記録

~~~py
from enum import Enum
import json
import yaml


class BaseObjectSerializer(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.value
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, object):
            ex = obj._excludes if hasattr(obj, '_excludes') else {}
            vals = obj._customes.copy() if hasattr(obj, '_customs') else {}
            vals.update(getattr(obj, '__dict__', {}))
            return dict([(k, v) for k, v in vals.items()
                         if k not in ex and not k.startswith('_') and v])

        return super(BaseObjectSerializer, self).default(obj)

    @classmethod
    def to_json(cls, obj, *args, **kwargs):
        return json.dumps(obj, cls=cls, *args, **kwargs)

    @classmethod
    def to_yaml(cls, obj, *args, **kwargs):
        return yaml.safe_dump(json.loads(cls.to_json(obj, *args, **kwargs)))
~~~
