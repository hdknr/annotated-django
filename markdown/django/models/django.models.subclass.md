# サブクラス

## 継承される親クラスにサブクラスの ContentTypeを持たせる

~~~py
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.utils.functional import cached_property


class SuperModel(models.Model):
    subclass_type = models.ForeignKey(
        ContentType, verbose_name=_("サブクラスタイプ"),
        null=True, blank=True, default=None,
        on_delete=models.SET_NULL)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self._meta.parents:
            # サブクラス(親がある)場合、自分のContentTypeを設定)
            self.subclass_type = ContentType.objects.get_for_model(self)
        super(SuperModel, self).save(*args, **kwargs)

    @cached_property
    def instance(self):
        # サブクラスがあれば実態のクラスのインスタンスに変換して返す
        return self.subclass_type and \
            self.subclass_type.get_object_for_this_type(id=self.id) or self
~~~