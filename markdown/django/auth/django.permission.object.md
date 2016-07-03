User.has_perm(user, perm, obj=None)


## モデルクラスに パーミッションチェッカーを実装

~~~py
class Event(models.Model):

    def has_perm(self, user, perm):
        # たとえば...
        if self.org.has_perm(user, perm):
            return True

        if perm == "events.browse_event":
            if self.is_private:
                return user.has_perm(perm)
            else:
                return True
~~~

## backends でオブジェクトパーミッションチェッカーを起動

- app/backends.py

~~~py
class PermissionBackend(object):
    def has_perm(self, user_obj, perm, obj=None):
        '''
        :param user_obj: User instance
        :param perm: permission code string (`auth.change_auth_user`)
        :param obj: Model instance (optional)
        '''
        res = obj and hasattr(obj, 'has_perm') and obj.has_perm(user_obj, perm)
        return res or False

    def authenticate(self, username=None, password=None):
        # required for Permission Backends
        pass
~~~

- app/settings.py

~~~py
from django.conf import global_settings                                          

AUTHENTICATION_BACKENDS = global_settings.AUTHENTICATION_BACKENDS + [            
'app.backends.PermissionBackend',                                           
]  
~~~


## views.py

~~~py
from django.http import HttpResponseForbidden

def event_edit(request, id):
    event = models.Event.objects.get(id=id)
    if not request.user.has_perm('events.change_event', event):
          return HttpResponseForbidden()
    ...
~~~    

## テンプレートフィルタ: `has_perm`

~~~py
@register.filter
def tup(src, arg):
    if isinstance(src, tuple):
        return src + (arg, )
    return (src, arg, )


@register.filter
def has_perm((obj, user), perm):
    return user.has_perm(perm, obj)
~~~

- detail.html  

~~~py
{% if event|tup:user|has_perm:'events.change_event' %}
  <a href="{% url 'events_event_edit' id=event.id %}">{% trans 'Edit' %}</a>
{% %}
~~~

## action 名からモデルへのパーミッションコードを返す

~~~py
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_permission_codename

class BaseModel(object):

    @classmethod
    def perm_name(cls, action, model=None):
        '''指定されたアクションに対するパーミッション名'''
        model = model or cls
        return "{}.{}".format(
            model._meta.app_label,
            get_permission_codename(action, model._meta))

~~~

## default_permissions

~~~py
class Event(models.Model):
    ....
    class Meta:
        default_permissions = ('add', 'change', 'delete', 'browse')
~~~

## テンプレートフィルタ: `can`

~~~py
@register.filter                                                                 
def can((obj, user), action):                                                    
    perm = models.BaseModel.perm_name(action, model=obj)                         
    return user.has_perm(perm, obj)    
~~~

~~~py
{% if event|tup:user|can:'change' %}
  <a href="{% url 'events_event_edit' id=event.id %}">{% trans 'Edit' %}</a>
{% %}
~~~
