- [decorating login_required Django decorator ](http://stackoverflow.com/questions/32187319/decorating-login-required-django-decorator)

~~~py
def check_permanent_password(user):
    return not user.temporary_password

@login_required(login_url)
@user_passes_test(check_temporary_password, login_url=settings.SET_PERMANENT_PASSWORD_URL)
def view(request):
      # your view
~~~    


## モデルに対するアクションがあるかどうかで判定


decorators.py:

~~~py
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def can(test_actions, model, login_url=None, raise_exception=False):

    def check_actions(user):
        actions = list(perms.actions_for(user, model, test_actions))
        if len(actions) < 0:
            if raise_exceptionreturn:
                raise PermissionDenied
            return False
        return True

    return user_passes_test(check_actions, login_url=login_url)
~~~

perms.py:

~~~py
from django.contrib.auth import get_permission_codename

def actions_for(user, model, possible):
    '''possible: list of actions '''
    return filter(lambda a: user.has_perm(perm_name(a, model)), possible)

def perm_name(action, model):
    return "{}.{}".format(
        model._meta.app_label, get_permission_codename(action, model))
~~~    


views.py:


~~~py

@can(['check', 'close'], models.Application)
def application_index(request):
    ....
~~~
