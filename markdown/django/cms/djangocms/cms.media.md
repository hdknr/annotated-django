## settings.MEDIA_URL

~~~py
MEDIA_URL = '/media/'
~~~


## settings.MEDIA_ROOT

~~~py
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
~~~



### 開発用の配信(urls)

urls.py:

~~~py
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

....

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
~~~        
