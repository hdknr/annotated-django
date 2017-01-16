# coding: utf-8
"""
Wrapper for loading templates from "templates" directories in INSTALLED_APPS
packages.
"""

from django.template.utils import get_app_template_dirs

from .filesystem import Loader as FilesystemLoader


class Loader(FilesystemLoader):
    # 実際はファイルシステムローダー

    def get_dirs(self):
        # アプリケーションのtemplatesディレクトリを全て返す
        return get_app_template_dirs('templates')
