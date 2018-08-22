# ファイルに保存されたメッセージをMySQLのテーブルに入れる(Python3/Django2.1)

- [19.1.2. email.parser: 電子メールメッセージのパース — Python 3.6.6 ドキュメント](https://docs.python.org/ja/3/library/email.parser.html) 
- 複数エンコードが含まれる可能性が高いので `バイナリ` で読み込む
- 格納は `TextField`(`longtext`) ではなく `BinaryField`(`longblob`)
- [smart_str](https://docs.djangoproject.com/ja/2.1/ref/utils/#django.utils.encoding.smart_str) で `str` に変換して `message_from_string` で復元する

~~~py
from django.db import models
from django.utils.functional import cached_property
from django.utils.encoding import smart_str

from email import message_from_string, message_from_binary_file
from email.utils import parseaddr


def parse_addresses(msgobj):
    _, from_address = parseaddr(msgobj['Return-Path'] or msgobj['From'])
    _, to_address = parseaddr(msgobj['Delivered-To'] or msgobj['To'])
    return from_address, to_address


class MesasgeQuerySet(models.QuerySet):

    def from_file(self, path, **kwargs):
        src =  open(path, 'rb')                 # 複数文字コードが含まれるファイル
        obj = message_from_binary_file(src)     # バイナリで読む
        return self.from_mailobject(obj, **kwargs)


    def from_mailobject(self, msgobj, **kwargs):
        sender, recipient = parse_addresses(msgobj)
        raw_message = msgobj.as_string().encode()   # str -> byte

        return self.create(
            sender=sender, recipient=recipient,
            raw_message=raw_message, **kwargs)


class Message(models.Model):
    subject = models.CharField(max_length=200)
    sender = models.EmailField()
    recipient = models.EmailField()
    raw_message = models.BinaryField()

    objects = MesasgeQuerySet.as_manager()

    @cached_property
    def mailobject(self):
        return message_from_string(
           smart_str(self.raw_message))

'''
SHOW CREATE TABLE emails_message;

CREATE TABLE `emails_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(200) NOT NULL,
  `sender` varchar(254) NOT NULL,
  `recipient` varchar(254) NOT NULL,
  `raw_message` longblob NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
'''
~~~