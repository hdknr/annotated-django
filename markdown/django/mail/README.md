[#44](https://github.com/hdknr/annotated-django/issues/44)

# Django

- [Sending email](https://docs.djangoproject.com/en/2.0/topics/email//)

## ショートカット

- [send_mail()](https://docs.djangoproject.com/en/2.0/topics/email/#send-mail)
- [send_mass_mail()](https://docs.djangoproject.com/en/2.0/topics/email/#send-mass-mail)
- [mail_admins()](https://docs.djangoproject.com/en/2.0/topics/email/#mail-admins)  : 管理者へメールする
- [mail_managers()](https://docs.djangoproject.com/en/2.0/topics/email/#mail-managers) : `MANAGERS` へメールする

## バックエンド

- `Email backends`
- [settings.EMAIL_BACKEND](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-EMAIL_BACKEND)

### 接続の維持

- [Sending multiple emails](https://docs.djangoproject.com/en/2.0/topics/email//#sending-multiple-emails)


1: バックエンドを生成して、メセージを複数渡す

~~~py
from django.core import mail
connection = mail.get_connection()    # Use default email connection
messages = get_notification_email()
connection.send_messages(messages)
~~~

デフォルト:
~~~py
In [5]: type(connection)
Out[5]: django.core.mail.backends.smtp.EmailBackend
~~~

2: EmailMessageにバックエンドを指定する

~~~py
from django.core import mail
con = mail.get_connection()
con.open()                   # 明示的にオープンする

def get_notification_email(user, con)
  subject = mail_subject(user)
  body = mail_body(user)
  return mail.EmailMessage(subejct, body, 'admin@mydom.com', [user.email])

for user in User.objects.all():
  email = get_notification_email(user, connection)
  email.send()

con.close()
~~~

## メッセージクラス

- [`EmailMessage` クラス](django.mails.EmailMesage.md)
- `EmailMultiAlternatives` クラス: [添付がある場合など](https://docs.djangoproject.com/ja/1.10/topics/email/#sending-alternative-content-types)

## その他

- [パスワードリセットメール]((django.mails.password_reset.md)
- [メールメッセージをlongblobに保存する](django.mails.messageobject.md)

# Projects

- [pinax/django-mailer](https://github.com/pinax/django-mailer)

## AWS SES

- [通知(SNS)メッセージJSONの検証](ses.veify-notification.md)
