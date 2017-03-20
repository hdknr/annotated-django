## フォームのフィールドエラー


- エラーをセット
- `mark_safe` すること！

~~~py
from django.utils.safestring import mark_safe as _S   

class UserSignupForm(forms.ModelForm):                                           
    ....  
    def clean_email(self):                                                          
        email = self.cleaned_data.get('email', None)                                
        if not email:                                                               
            raise forms.ValidationError(                                            
                _S(_("Email is required.")))                                        
        if get_user_model().objects.filter(username=email).exists():                
            raise forms.ValidationError(                                            
                _S(_("Email address has been registred.")))                         
        return email   
~~~

- poファイルにHTMLメッセージ
- リンクを埋め込みたいエリアにCSSクラスを入れる

~~~
"あるいはメールが届いていない場合は<span class=\"password-reset\">こちら</span>からリセット"
~~~

- jQueryでURLを埋め込む

~~~js
$("input[name='email']")
  .parents('div')
  .find('div.help-block .password-reset')
  .html('<a href="{% url 'accounts_password_reset' %}">こちら</a>');
~~~
