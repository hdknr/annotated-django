## エラーコード指定


~~~py
from django.http import HttpResponse

def index(request):
    ...
    return HttpResponse(status=500)     # 500 ERROR
~~~     

## 403

~~~py
from django.core.exceptions import PermissionDenied

def index(request):
  ...
  raise PermissionDenied
~~~

## 404

~~~py
from django.http import Http404

def index(request):
  ...
  raise Http404
~~~


## 500

~~~py
from django.http import HttpResponseServerError

def index(request):
  ...
  return HttpResponseServerError()
~~~
