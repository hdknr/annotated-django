# coding: utf-8
"""
This module allows importing AbstractBaseSession even
when django.contrib.sessions is not in INSTALLED_APPS.
"""
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


class BaseSessionManager(models.Manager):
    '''マネージャ'''

    def encode(self, session_dict):
        """
        Return the given session dictionary serialized and encoded as a string.
        """
        # セッションストアクラスを取得して、encode(データ辞書) する
        session_store_class = self.model.get_session_store_class()
        return session_store_class().encode(session_dict)

    def save(self, session_key, session_dict, expire_date):
        s = self.model(session_key, self.encode(session_dict), expire_date)
        if session_dict:
            s.save()
        else:
            s.delete()  # Clear sessions with no data.
        return s


@python_2_unicode_compatible
class AbstractBaseSession(models.Model):
    '''抽象セッションモデル'''
    session_key = models.CharField(_('session key'), max_length=40, primary_key=True)
    '''セッションキー'''
    session_data = models.TextField(_('session data'))
    '''セッションキーデータ'''
    expire_date = models.DateTimeField(_('expire date'), db_index=True)
    '''有効期限'''

    objects = BaseSessionManager()

    class Meta:
        abstract = True				# 抽象モデル
        verbose_name = _('session')
        verbose_name_plural = _('sessions')

    def __str__(self):
        return self.session_key

    @classmethod
    def get_session_store_class(cls):
        raise NotImplementedError

    def get_decoded(self):
        '''デコードして辞書を返す'''
        # デフォルトで django.contrib.sessions.backends.db.SessionStore
        session_store_class = self.get_session_store_class()
        return session_store_class().decode(self.session_data)
