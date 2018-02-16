- [#43](https://github.com/hdknr/annotated-django/issues/43)

## WeasyPrint

- https://github.com/Kozea/WeasyPrint

### インストール

~~~bash
$ sudo apt-get install build-essential python3-dev python3-pip python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
~~~

~~~bash
$ pip install WeasyPrint
~~~

### テンプレートレンダリングの結果をPDFで返す

~~~py
from django.http import HttpResponse
from mimetypes import guess_type
from weasyprint import HTML


class HtmlToPdfResponse(HttpResponse):

    def __init__(
        self, content='', filename=None,
        content_type='application/octet-stream', *args, **kwargs
    ):
        content_type = filename and guess_type(filename)[0] or content_type

        super(HtmlToPdfResponse, self).__init__(
            content, content_type=content_type, *args, **kwargs)

        self.write(HTML(string=content).write_pdf())

        if filename:
            self.set_filename(filename)

    def set_filename(self, filename):
        self['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
~~~

~~~py
from django.template import loader

def render_by(name, request=None, **kwargs):
    return loader.get_template(name).render(context=kwargs)
~~~

~~~py
from . import utils, responses, models

def application_pdf(request, id):
    instance = models.Application.objects.filter(id=id).first()
    name = instance.title + ".pdf"
    html = utils.render_by('webentry/application/pdf.html', instance=instance)
    return responses.HtmlToPdfResponse(html, filename=name)
~~~


## その他

- [Outputting PDFs with Django](https://docs.djangoproject.com/en/2.0/howto/outputting-pdf/)
