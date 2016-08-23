派生クラスへのインスタンス


~~~py
from django.db.models.fields.related import OneToOneRel


class BaseModel(models.Model):

    @property
    def instance(self):
        def _cache():
            self._instance = self
            for i in self._meta.related_objects:
                if all([
                    isinstance(i, OneToOneRel),
                    issubclass(i.related_model, self._meta.model)
                ]):
                    self._instance = i.related_model.objects.filter(
                        **{i.field_name: self.id}).first()
                    if self._instance:
                        break
            self._instance = self._instance or self
            return self._instance

        return getattr(self, '_instance', _cache())    
~~~
