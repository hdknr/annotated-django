
~~~py
@never_cache                                                                        
@csrf_exempt                                                                        
@psa('{0}:complete'.format(NAMESPACE))                                              
def complete(request, backend, *args, **kwargs):                                    
    """Authentication complete view"""                                              
    return do_complete(request.backend, _do_login, request.user,                    
                       redirect_name=REDIRECT_FIELD_NAME, *args, **kwargs)  
~~~                       


# actions.py

~~~py
def do_complete(backend, login, user=None, redirect_name='next', *args, **kwargs):                                                   
    data = backend.strategy.request_data()                                          

    # すでに認証すみか？                                                                                       
    is_authenticated = user_is_authenticated(user)                                  
    user = is_authenticated and user or None                                        

    # パーシャルデータ復元                                                                                    
    partial = partial_pipeline_data(backend, user, *args, **kwargs)                 
    if partial:                                                                     
        xargs, xkwargs = partial                                                    
        user = backend.continue_pipeline(*xargs, **xkwargs)                         
    else:                                                                           
        # パーシャルがないので完了
        user = backend.complete(user=user, *args, **kwargs)                         

    # セッションからリダイレクト情報を取得する                                                                                    
    redirect_value = backend.strategy.session_get(redirect_name, '') or \           
                     data.get(redirect_name, '')                                    

    # ユーザーのモデル確認
    user_model = backend.strategy.storage.user.user_model()                         
    if user and not isinstance(user, user_model):                                   
        return user        

    # ここより先は次のリダイレクトを判定

    if is_authenticated:                                                            
        # 認証すみ
        if not user:                                                                
            url = setting_url(backend, redirect_value, 'LOGIN_REDIRECT_URL')        
        else:                                                                       
            url = setting_url(backend, redirect_value,                           
                              'NEW_ASSOCIATION_REDIRECT_URL',                    
                              'LOGIN_REDIRECT_URL')                              
    elif user:                                                                   
        # 認証していないユーザー
        if user_is_active(user):                                                 
            # 有効なユーザー
            # catch is_new/social_user in case login() resets the instance       
            is_new = getattr(user, 'is_new', False)                              
            social_user = user.social_user                                       
            login(backend, user, social_user)                                    
            # store last login backend name in session                           
            backend.strategy.session_set('social_auth_last_login_backend',       
                                         social_user.provider)                   

            if is_new:                                                           
                url = setting_url(backend,                                       
                                  'NEW_USER_REDIRECT_URL',                       
                                  redirect_value,                                
                                  'LOGIN_REDIRECT_URL')                          
            else:                                                                
                url = setting_url(backend, redirect_value,                       
                                  'LOGIN_REDIRECT_URL')                          
        else:                                                                    
            # 無効なユーザー
            if backend.setting('INACTIVE_USER_LOGIN', False):                    
                social_user = user.social_user                                   
                login(backend, user, social_user)                                
            url = setting_url(backend, 'INACTIVE_USER_URL', 'LOGIN_ERROR_URL',   
                              'LOGIN_URL')                                       
    else:                                                                        
        # エラー
        url = setting_url(backend, 'LOGIN_ERROR_URL', 'LOGIN_URL')               


    # URLの検証
    if redirect_value and redirect_value != url:                                 
        redirect_value = quote(redirect_value)                                   
        url += ('?' in url and '&' or '?') + \                                   
               '{0}={1}'.format(redirect_name, redirect_value)                   

    if backend.setting('SANITIZE_REDIRECTS', True):                              
        allowed_hosts = backend.setting('ALLOWED_REDIRECT_HOSTS', []) + \        
                        [backend.strategy.request_host()]                        
        url = sanitize_redirect(allowed_hosts, url) or \                         
              backend.setting('LOGIN_REDIRECT_URL')                              

    # 実際のリダイレクト
    return backend.strategy.redirect(url)      
~~~
