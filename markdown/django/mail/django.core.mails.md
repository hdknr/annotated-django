django.core.mails.get_connection():

~~~py
from django.utils.module_loading import import_string

def get_connection(backend=None, fail_silently=False, **kwds):
    klass = import_string(backend or settings.EMAIL_BACKEND)
    return klass(fail_silently=fail_silently, **kwds)
~~~
