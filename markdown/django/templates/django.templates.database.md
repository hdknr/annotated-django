

## カスタムローダ

- [Custom Loaders](https://docs.djangoproject.com/ja/1.10/ref/templates/api/#custom-loaders)
- [django.template.loaders](https://github.com/django/django/tree/master/django/template/loaders)

TODO:

- django.template.loaders.base.Loader を継承する
- get_contents() を実装する
- get_template_sources() を実装する


### settings

~~~py
In [1]: from django.conf import settings
In [2]: settings.TEMPLATES[0]
Out[2]:
{'APP_DIRS': True,
 'BACKEND': 'django.template.backends.django.DjangoTemplates',
 'DIRS': [],
 'OPTIONS': {'context_processors': ['django.contrib.auth.context_processors.auth',
   'django.template.context_processors.debug',
   'django.template.context_processors.i18n',
   'django.template.context_processors.media',
   'django.template.context_processors.static',
   'django.template.context_processors.tz',
   'django.contrib.messages.context_processors.messages',
   'django.template.context_processors.request',
   'social.apps.django_app.context_processors.backends',
   'social.apps.django_app.context_processors.login_redirect'],
  'debug': True}}
~~~

## django-dbtemplates

- [django-dbtemplates](https://django-dbtemplates.readthedocs.io/en/latest/)
- [jazzband/django-dbtemplates](https://github.com/jazzband/django-dbtemplates)

Loader:

- [dbtemplates.loader.Loader](https://github.com/jazzband/django-dbtemplates/blob/master/dbtemplates/loader.py)

### dbtemplate を優先にする

settings.py: `loaders` のリストの先頭にする

~~~py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                ......
            ],
            'loaders': [
                'dbtemplates.loader.Loader',                
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]
~~~

#### リロード

- `content` をブランクにして保存するとリロードする

~~~py
class Template(models.Model):                                                    

    def save(self, *args, **kwargs):                                                
        self.last_changed = now()                                                   
        # If content is empty look for a template with the given name and           
        # populate the template instance with its content.                          
        if settings.DBTEMPLATES_AUTO_POPULATE_CONTENT and not self.content:         
            self.populate()                                                         
        super(Template, self).save(*args, **kwargs)   
~~~
