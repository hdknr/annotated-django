# 抽象モデル

## 抽象モデルのシリアライザーを生成する

指定したモデルクラスのシリアライザクラスを動的に作成する:

~~~py
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework.utils.field_mapping import get_field_kwargs

def factory(cls, base=Serializer):
    def _map(field):
        field_class = ModelSerializer.serializer_field_mapping.get(type(field), None)
        kwargs = get_field_kwargs(field.name, field)
        kwargs.pop('model_field', None)
        return field_class and field_class(**kwargs)

    fields = dict((field.name, _map(field)) for field in cls._meta.fields)
    return type(cls._meta.object_name + "Serializer", (base, ), fields)
~~~

例:

~~~py
from .models import Message   # 抽象(abstract = True)モデル


class BaseSerializer(Serializer):

    def create(self, validate_data):
        # TODO: save validate_data
        # ......
        return Message(**validate_data)

MessageSerializer = factory(Message, base=BaseSerializer)
~~~

## メタクラスで同様に

~~~py
from rest_framework.serializers import (
  Serializer, SerializerMetaclass, ModelSerializer)
from rest_framework.utils.field_mapping import get_field_kwargs
from collections import OrderedDict


class AbstractModelMetaclass(SerializerMetaclass):

    def __new__(cls, name, bases, attrs):
        meta = attrs.get('Meta', None)
        fields = cls._get_declared_fields(bases, attrs)
        fields = meta and cls.fields_from_model(meta.model, **fields) or fields
        attrs['_declared_fields'] = fields
        return type.__new__(cls, name, bases, attrs)

    @classmethod
    def fields_from_model(cls, model_class, **others):

        def _map(field):
            field_class = ModelSerializer.serializer_field_mapping.get(type(field), None)
            kwargs = get_field_kwargs(field.name, field)
            kwargs.pop('model_field', None)
            return field_class and field_class(**kwargs)

        return OrderedDict(
            [(field.name, _map(field)) for field in model_class._meta.fields], **others)
~~~

~~~py
class MessageSerializer(Serializer, metaclass=AbstractModelMetaclass):

    class Meta:
        model = Message

    def create(self, validate_data):
        # TODO: save validate_data
        # ......
        return Message(**validate_data)
~~~
