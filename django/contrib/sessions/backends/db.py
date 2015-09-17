# -*- coding: utf-8 -*-
'''SessionStore:

- データベースでセッションを管理します。
- logging するのであれば `django.security.SessionStore` のロガーを定義すること

'''
import logging

from django.contrib.sessions.backends.base import CreateError, SessionBase
from django.core.exceptions import SuspiciousOperation
from django.db import IntegrityError, router, transaction
from django.utils import timezone
from django.utils.encoding import force_text


class SessionStore(SessionBase):
    """
    Implements database session store.
    """
    def __init__(self, session_key=None):
        super(SessionStore, self).__init__(session_key)

    def load(self):
        '''ロード(session_dataをdecodeして返す)

        :rtype: dict
        '''
        try:
            s = Session.objects.get(
                session_key=self.session_key,
                expire_date__gt=timezone.now()
            )
            return self.decode(s.session_data)
        except (Session.DoesNotExist, SuspiciousOperation) as e:
            if isinstance(e, SuspiciousOperation):
                logger = logging.getLogger(
                    'django.security.%s' % e.__class__.__name__)
                logger.warning(force_text(e))
            self._session_key = None
            return {}

    def exists(self, session_key):
        '''セッションキーのセッションの存在確認 '''
        return Session.objects.filter(session_key=session_key).exists()

    def create(self):
        '''ユニークなセッションキーで新規セッションを作成する'''
        while True:
            self._session_key = self._get_new_session_key()
            try:
                # Save immediately to ensure we have a unique entry in the
                # database.
                self.save(must_create=True)
            except CreateError:
                # Key wasn't unique. Try again.
                continue
            self.modified = True
            return

    def save(self, must_create=False):
        """
        Saves the current session data to the database. If 'must_create' is
        True, a database error will be raised if the saving operation doesn't
        create a *new* entry (as opposed to possibly updating an existing
        entry).

        - データベースルーターからSessionモデル用の
          データベースを取得してそこに保存する
        """
        if self.session_key is None:
            return self.create()
        obj = Session(
            session_key=self._get_or_create_session_key(),
            session_data=self.encode(self._get_session(no_load=must_create)),
            expire_date=self.get_expiry_date()
        )
        using = router.db_for_write(Session, instance=obj)
        try:
            with transaction.atomic(using=using):
                obj.save(force_insert=must_create, using=using)
        except IntegrityError:
            if must_create:
                raise CreateError
            raise

    def delete(self, session_key=None):
        '''キーのセッションを削除する'''
        if session_key is None:
            if self.session_key is None:
                return
            session_key = self.session_key
        try:
            Session.objects.get(session_key=session_key).delete()
        except Session.DoesNotExist:
            pass

    @classmethod
    def clear_expired(cls):
        '''時間切れセッションを全て削除します'''
        Session.objects.filter(expire_date__lt=timezone.now()).delete()

# At bottom to avoid circular import
from django.contrib.sessions.models import Session  # isort:skip
