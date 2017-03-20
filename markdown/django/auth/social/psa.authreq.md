## 認証リクエスト

### Djanogでの認証リクエストURLテンプレート設置

~~~html

<a href="{% url 'social:begin' backend='facebook'  %}?{{ request.GET.urlencode }}">
  <i class="fa fa-facebook-official" aria-hidden="true"></i>  {# Fontawesome #}
  {% trans 'Facebook Login' %} </a>
~~~


### 認証リクエストのビューハンドラ

~~~py
from social.actions import do_auth

@never_cache
@psa('{0}:complete'.format(NAMESPACE))
def auth(request, backend):
    return do_auth(request.backend, redirect_name=REDIRECT_FIELD_NAME)
~~~~

- REDIRECT_FIELD_NAME は デフォルト `next`

~~~py
In [7]: from django.contrib.auth import login, REDIRECT_FIELD_NAME

In [8]: REDIRECT_FIELD_NAME
Out[8]: 'next'
~~~


### 認証リクエストの実際のアクション

~~~py
def do_auth(backend, redirect_name='next'):                                         
    backend.strategy.clean_partial_pipeline()  # パーシャルデータは削除                                         

    data = backend.strategy.request_data(merge=False) # next の値をセッションに保存

    # その他の追加データをセッションに保存
    for field_name in backend.setting('FIELDS_STORED_IN_SESSION', []):              
        if field_name in data:                                                      
            backend.strategy.session_set(field_name, data[field_name])              

    if redirect_name in data:                                                       
        # Check and sanitize a user-defined GET/POST next field value               
        redirect_uri = data[redirect_name]    # next の値                                         
        if backend.setting('SANITIZE_REDIRECTS', True):                             
            allowed_hosts = backend.setting('ALLOWED_REDIRECT_HOSTS', []) + \       
                            [backend.strategy.request_host()]                       
            redirect_uri = sanitize_redirect(allowed_hosts, redirect_uri)           

        backend.strategy.session_set(                                               
            redirect_name,                                                          
            redirect_uri or backend.setting('LOGIN_REDIRECT_URL')                   
        )                                                                           
    return backend.start()               
~~~    

### バックエンドでの認証リクエストの開始


~~~py
class BaseAuth(object):                                                             

    def start(self):                                                                
        self.strategy.clean_partial_pipeline()                                      
        if self.uses_redirect():                                                    
            # リダイレクトを使うバックエンドだとリダイレクトを返す
            return self.strategy.redirect(self.auth_url())                          
        else:                                                                       
            return self.strategy.html(self.auth_html())    

    def uses_redirect(self):                                                        
        # デフォルトはリダイレクト
        return True       
~~~            

### Django ストラテジ

~~~py
from django.shortcuts import redirect                                            

class DjangoStrategy(BaseStrategy):                                                 

  def redirect(self, url):                                                     
      return redirect(url)    
~~~
