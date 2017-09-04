http://docs.django-cms.org/en/release-3.4.x/introduction/third_party.html


## settings.INSTALLED_APPS

~~~py
In [3]: settings.INSTALLED_APPS
Out[3]:
('djangocms_admin_style',
 'django.contrib.auth',
 'django.contrib.contenttypes',
 'django.contrib.sessions',
 'django.contrib.admin',
 'django.contrib.sites',
 'django.contrib.sitemaps',
 'django.contrib.staticfiles',
 'django.contrib.messages',
 'cms',
 'menus',
 'sekizai',
 'treebeard',
 'djangocms_text_ckeditor',
 'filer',
 'easy_thumbnails',
 'djangocms_column',
 'djangocms_link',
 'cmsplugin_filer_file',
 'cmsplugin_filer_folder',
 'cmsplugin_filer_image',
 'cmsplugin_filer_utils',
 'djangocms_style',
 'djangocms_snippet',
 'djangocms_googlemap',
 'djangocms_video',
 'mysite')
~~~


## settings.THUMBNAIL_PROCESSORS

~~~py
In [2]: settings.THUMBNAIL_PROCESSORS
Out[2]:
('easy_thumbnails.processors.colorspace',
 'easy_thumbnails.processors.autocrop',
 'filer.thumbnail_processors.scale_and_crop_with_subject_location',
 'easy_thumbnails.processors.filters')
~~~


## settings.STATICFILES_FINDERS

~~~py
In [4]: settings.STATICFILES_FINDERS
Out[4]:
['django.contrib.staticfiles.finders.FileSystemFinder',
 'django.contrib.staticfiles.finders.AppDirectoriesFinder']
~~~


## settings.TEMPLATES

~~~py
In [5]: settings.TEMPLATES
Out[5]:
[{'BACKEND': 'django.template.backends.django.DjangoTemplates',
  'DIRS': ['/vagrant/projects/hdknr/mysite/mysite/templates'],
  'OPTIONS': {'context_processors': ['django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.template.context_processors.i18n',
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.template.context_processors.media',
    'django.template.context_processors.csrf',
    'django.template.context_processors.tz',
    'sekizai.context_processors.sekizai',
    'django.template.context_processors.static',
    'cms.context_processors.cms_settings'],
   'loaders': ['django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader']}}]
~~~



- [Aldryn News & Blog](3rdparty/aldryn-newsblog.md)
