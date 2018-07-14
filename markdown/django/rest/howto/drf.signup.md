## ユーザー登録例


### ViewSet


~~~py
from rest_framework import (
    permissions, viewsets, response, decorators, status)
from django.core.exceptions import ValidationError
from . import serializers, models, signals

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = models.Profile.objects.all()

    @decorators.action(
        methods=['post'], detail=False, 
        permission_classes=[permissions.AllowAny]
    )
    def signup(self, request):
        ## save()処理(実際はcreate)
        serializer = serializers.SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # 有効化を行うURLをメールで送る
        signals.profile_activate_mail.send(
                context=context{'request': request}, 
                instance=serializer.instance)

        return response.Response(serializer.data)

    def handle_exception(self, exc):
        # (override) ValidationError を処理する
        try:
            return super(BaseViewSet, self).handle_exception(exc)
        except ValidationError:
            content = {'detail': list(exc.messages)}
            return response.Response(content, status=status.HTTP_400_BAD_REQUEST)
~~~

### Serializer

~~~py
from rest_framework import serializers
from . import models

class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = models.Profile
        exclude = ['number', 'user']

    def create(self, validate_data):
        username = validate_data.pop('username')
        password = validate_data.pop('password')
        return models.Profile.objects.provide(username, password, **validate_data)
~~~

### QuerySet

~~~py
from django.db import models
from django.contrib.auth.models import User
from .validations import validate_credentials


class AccountQuerySet(models.QuerySet):

    def provide(self, username, password, **params):
        # 無効ユーザーを作る(メールに添付されたURLをクリックして有効化させる)
        user = User(username=username, email=username, is_active=False)
        validate_credentials(user, password)
        user.set_password(password)
        user.save()
        return self.create(user=user, **params)
~~~


### Validators

~~~py
from django.contrib.auth import password_validation, get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class UserExistsException(Exception):
    def __init__(self, user, message=''):
        message = _('User {user} already exists. {message}').format(
            user=user, message=message)
        super().__init__(message)


def available_username(name):
    return not get_user_model().objects.filter(username=name).exists()


def validate_usernname(username, username_validators=None):
    errors = []
    if username_validators:
        for validator in username_validators:
            try:
                validator.validate(username)
            except ValidationError as error:
                errors.append(error)

    if not available_username(username):
        errors.append(UserExistsException(username))

    if errors:
        raise ValidationError(errors)


def validate_credentials(user, password, username_validators=None, password_validators=None):
    password_validation.validate_password(password, user, password_validators=password_validators)
    validate_usernname(user.username, username_validators=username_validators)
~~~

