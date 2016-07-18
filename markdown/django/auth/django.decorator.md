- [decorating login_required Django decorator ](http://stackoverflow.com/questions/32187319/decorating-login-required-django-decorator)

~~~py
def check_permanent_password(user):
    return not user.temporary_password

@login_required(login_url)
@user_passes_test(check_temporary_password, login_url=settings.SET_PERMANENT_PASSWORD_URL)
def view(request):
    # your view
~~~    
