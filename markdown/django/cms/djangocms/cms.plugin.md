- [plugin](http://docs.django-cms.org/en/release-3.4.x/introduction/plugins.html)


## plugin モデル

- [プラグインモデル](http://docs.django-cms.org/en/release-3.4.x/introduction/plugins.html#the-plugin-model)

## plugin クラス

- [プラグインクラス](http://docs.django-cms.org/en/release-3.4.x/introduction/plugins.html#the-plugin-class)



## 基本プラグイン

- [Some commonly-used plugins](http://docs.django-cms.org/en/release-3.4.x/topics/commonly_used_plugins.html#commonly-used-plugins)


djangocms-installer でデフォルトで入ります:

- [django-filer](cms.filer.md)
- https://github.com/divio/djangocms-link
- https://github.com/divio/djangocms-file
- https://github.com/divio/djangocms-picture
- https://github.com/divio/djangocms-video
- [djangocms-googlemap](cms.googlemap.md)
- https://github.com/divio/djangocms-snippet
- https://github.com/divio/djangocms-style
- https://github.com/divio/djangocms-column


~~~py
INSTALLED_APPS = [
    ...
    'djangocms_link',
    'djangocms_file',
    'djangocms_picture',
    'djangocms_video',
    'djangocms_googlemap',
    'djangocms_snippet',
    'djangocms_style',
    'djangocms_column',
    ...
]
~~~
