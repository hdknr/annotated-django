# sample2 

~~~py
from django.db.models import Model
from django.contrib.auth.models import User
from rest_framework import serializers, fields
from myaccounts import utils, exceptions
from myaccounts.validations import validate_credentials
from collections import OrderedDict
from accounts import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        exclude = ['password']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, required=False)

    class Meta:
        model = models.Profile
        fields = '__all__'

    def to_representation(self, value):
        res = super().to_representation(value)

        request = self.context.get('request', None)
        if request and (request.user == value.user or request.user.is_staff):
            # 本人か管理者であれば、そのままかえす(全情報)
            return res

        # それ以外であれあば、間引きした公開情報のみ
        user = OrderedDict((('id', res['user']['id']), ))
        return OrderedDict((
            ('id', res['id']),
            ('nickname', res['nickname']),
            ('user', user),
        ))


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = models.Profile
        exclude = ['number', 'mautic_id', 'user']

    def create(self, validate_data):
        username = validate_data.pop('username')
        password = validate_data.pop('password')
        # プロビジョニング
        # username, password で User作成し、これをつかって新しくProfileを作成
        return models.Profile.objects.provide(username, password, **validate_data)
~~~