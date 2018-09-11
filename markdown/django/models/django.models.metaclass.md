# メタクラス

- [メタクラス実装](https://github.com/hdknr/annotated-django/commit/1942069dff16e221500f5e4e48fe54e08985578c)

## カスタマイズ

~~~py
from django.db import models


class ProfileMeta(models.base.ModelBase):

    def __new__(cls, name, bases, attrs):
        # 先に何かする
        result = super(ProfileMeta, cls).__new__(cls, name, bases, attrs)
        # result をなにかいじる
        return result

class Profile(models.Model, metaclass=ProfileMeta):
    ....
~~~