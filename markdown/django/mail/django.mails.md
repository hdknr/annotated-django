- [Checking validity of email in django/python](http://stackoverflow.com/questions/3217682/checking-validity-of-email-in-django-python)


##  正規表現

- [http://emailregex.com/](http://emailregex.com/)

~~~python
r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
~~~




- [メールアドレスを表す現実的な正規表現](http://qiita.com/sakuro/items/1eaa307609ceaaf51123)

## Django

- [Dajngo 1.10検証](https://github.com/hdknr/annotated-django/commit/f725fe06f18bdf525aa91fcc4ef4b33c486c2c22)

~~~py
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
try:
    validate_email("foo.bar@baz.qux")
except ValidationError as e:
    print "oops! wrong email"
else:
    print "hooray! email is valid"
~~~

~~~py
from django.forms import EmailField
from django.core.exceptions import ValidationError

def isEmailAddressValid( email ):
    try:
        EmailField().clean(email)
        return True
    except ValidationError:
        return False
~~~        

- [テンプレートメール](django.mails.template.md)

### ガラケーRFC違反アドレス対応

- [django.contrib.auth.admin.UserAdmin の email をガラケーに対応させる](http://moqada.hatenablog.com/entry/20120901/1346521747)

Address.get_on_valid('hama..okamoto0953@docomo.ne.jp')
