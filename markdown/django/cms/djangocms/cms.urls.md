URLConf


- http://docs.django-cms.org/en/release-3.4.x/how_to/install.html#further-required-configuration

基本:

~~~py
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('cms.urls')),         # django-cms
]
~~~
