# Django

- [Sending email](https://docs.djangoproject.com/ja/1.10/topics/email/)

## ショートカット
- `send_mail()`
- `send_mass_mail()`
- `mail_admins()`  : 管理者へメールする
- `mail_managers()` : `MANAGERS` へメールする

## バックエンド

- `Email backends`

## メッセージクラス

- [`EmailMessage` クラス](django.mails.EmailMesage.md)
- `EmailMultiAlternatives` クラス: [添付がある場合など](https://docs.djangoproject.com/ja/1.10/topics/email/#sending-alternative-content-types)

## その他

- [パスワードリセットメール]((django.mails.password_reset.md)

# Projects

- [pinax/django-mailer](https://github.com/pinax/django-mailer)
- [hdknr/flier](https://github.com/hdknr/flier)
