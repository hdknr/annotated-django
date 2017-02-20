Trumbowyg: WYSIWYG widget

- https://alex-d.github.io/Trumbowyg/


## requirements.txt

~~~
bambu-bootstrap
django-bootstrap3
django-bower
~~~

~~~bash
$ pip install requirements.txt
~~~

## settings.py

~~~py
# BOWER
BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components/')
BOWER_INSTALLED_APPS = [
    'jquery',
    'bootstrap',
    'trumbowyg',        # WYSWYG editor
]
from django.conf import global_settings
STATICFILES_FINDERS = global_settings.STATICFILES_FINDERS + [
    'djangobower.finders.BowerFinder',
]
INSTALLED_APPS += [
    'djangobower',      # django-bower
]
~~~

~~~bash
$ python manage.py bower install
bower trumbowyg#*               cached https://github.com/Alex-D/Trumbowyg.git#2.4.2
bower trumbowyg#*             validate 2.4.2 against https://github.com/Alex-D/Trumbowyg.git#*
bower jquery#*                  cached https://github.com/jquery/jquery-dist.git#3.1.1
bower jquery#*                validate 3.1.1 against https://github.com/jquery/jquery-dist.git#*
bower bootstrap#*               cached https://github.com/twbs/bootstrap.git#3.3.7
bower bootstrap#*             validate 3.3.7 against https://github.com/twbs/bootstrap.git#*
~~~

## wyg.widgets.EditorWidget

~~~bash
$ python startapp wyg
~~~

- widgets.py

~~~py
from django.forms.widgets import Textarea
from django.utils.safestring import mark_safe
from django.utils import translation
from json import dumps


class EditorWidget(Textarea):

    class Media:
        css = {
            'all': (
                'bootstrap/dist/css/bootstrap.min.css',
                'trumbowyg/dist/ui/trumbowyg.css',
            )
        }

        js = (
            'jquery/dist/jquery.min.js',
            'bootstrap/dist/js/bootstrap.min.js',
            'trumbowyg/dist/trumbowyg.min.js',
        )

    def __init__(self, attrs=None, buttons=None):
        super(EditorWidget, self).__init__(attrs=None)

        self.editor = {}      # Trumbowygパラメータ

        # 必要なボタン
        if buttons:
            self.editor['btns'] = buttons

        # 言語
        lang = translation.get_language()
        if lang:
            self.editor['lang'] = lang
            js = 'trumbowyg/dist/langs/%s.min.js' % lang
            if js not in self.Media.js:
                self.Media.js += (js, )

    def render(self, name, value, attrs=None):
        output = super(EditorWidget, self).render(name, value, attrs)
        script = u'''
            <script> $('#id_%s').trumbowyg(%s); </script>
        ''' % (name, dumps(self.editor))
        output += mark_safe(script)
        return output
~~~        

## blogs.admin.EntryAdminForm

~~~bash
$ python startapp blogs
~~~

- models.py

~~~py
from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
~~~    

- admin.py

~~~py
from wyg.widgets import EditorWidget

class EntryAdminForm(ModelForm):

    class Meta:
        model = Entry
        exclude = []
        # 太字、イタリック、 URL挿入 のみゆるしてみる
        widgets = {
            'text': EditorWidget(buttons=[['bold', 'italic'], ['link']]),
        }
        # https://alex-d.github.io/Trumbowyg/documentation.html#button-pane


class EntryAdmin(admin.ModelAdmin):
    form = EntryAdminForm
~~~

## 表示

- settings.py

~~~py
INSTALLED_APPS += [
    'djangobower',      # django-bower
    'blogs',            # sample
]
~~~

![](https://github.com/hdknr/annotated-django/raw/master/markdown/django/wysiwyg/django-trumbowyg.png)
