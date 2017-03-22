
## フィールド

- [Using Validators](https://docs.djangoproject.com/en/1.10/ref/forms/validation/#using-validators)

~~~py
from django.forms import CharField
from django.core import validators

class SlugField(CharField):
    default_validators = [validators.validate_slug]
~~~

~~~py
slug = forms.CharField(validators=[validators.validate_slug])
~~~


## clean

~~~py
import re

class EmailForwardForm(forms.Form):

  def clean(self):                                                                
      user = self.cleaned_data.get('user', '')                                    

      if not re.search(EmailValidatorEx.user_regex, user):                        
          self.add_error('user', _(u'Invaid Address'))                            
      elif Forwarder.objects.filter(address=self.address).exists():               
          self.add_error('user', _(u'Address exits'))                             

      return self.cleaned_data   
~~~  
