## 認証応答ランディング(AuthRes):social_django.views.do_complete

### psa デコレータ

- [social_django.utils.psa](https://github.com/python-social-auth/social-app-django/blob/master/social_django/utils.py#L31) でバックエンドを見つける

~~~py
def psa(redirect_uri=None, load_strategy=load_strategy):
    def decorator(func):
        @wraps(func)
        def wrapper(request, backend, *args, **kwargs):
            uri = redirect_uri
            if uri and not uri.startswith('/'):
                uri = reverse(redirect_uri, args=(backend,))
            request.social_strategy = load_strategy(request)
            # backward compatibility in attribute name, only if not already
            # defined
            if not hasattr(request, 'strategy'):
                request.strategy = request.social_strategy

            try:
                # バックエンドを見つけます
                request.backend = load_backend(
                    request.social_strategy,    # django strategy
                    backend,                    # bakend名
                    uri)                        # redirect_uri

            except MissingBackend:
                raise Http404('Backend not found')
            return func(request, backend, *args, **kwargs)
        return wrapper
    return decorator
~~~    
~~~py
from social_core.backends.utils import get_backend
BACKENDS = settings.AUTHENTICATION_BACKENDS
STRATEGY = getattr(settings, setting_name('STRATEGY'),
                   'social_django.strategy.DjangoStrategy')

def load_backend(strategy, name, redirect_uri):
    Backend = get_backend(BACKENDS, name)
    return Backend(strategy, redirect_uri)


def load_strategy(request=None):
    return get_strategy(STRATEGY, STORAGE, request)
~~~


### complete

- [social_django.views.do_complete](https://github.com/python-social-auth/social-app-django/blob/master/social_django/views.py#L29)にランディング
- URLでbackend, ユーザー(ログインしていたら)がわかる(Facebook, Google, Amazon...)ので、このバックエンドとユーザーを指定して [social_core.actions.do_complete](https://github.com/python-social-auth/social-core/blob/master/social_core/actions.py#L30) にデレゲート

~~~py
@never_cache
@csrf_exempt
@psa('{0}:complete'.format(NAMESPACE))
def complete(request, backend, *args, **kwargs):
    """Authentication complete view"""
    return do_complete(
        request.backend,
        _do_login,
        request.user,
        redirect_name=REDIRECT_FIELD_NAME,
        request=request,                      # django : WSGI Requestを渡す
        *args, **kwargs)
~~~                       

~~~py
def _do_login(
    backend,      # バックエンドクラス
    user,         # ユーザー
    social_user
):
    user.backend = '{0}.{1}'.format(backend.__module__,
                                    backend.__class__.__name__)
    # Get these details early to avoid any issues involved in the
    # session switch that happens when we call login().
    enable_session_expiration = backend.setting('SESSION_EXPIRATION', False)
    max_session_length_setting = backend.setting('MAX_SESSION_LENGTH', None)

    # Log the user in, creating a new session.
    login(backend.strategy.request, user)

    # Make sure that the max_session_length value is either an integer or
    # None. Because we get this as a setting from the backend, it can be set
    # to whatever the backend creator wants; we want to be resilient against
    # unexpected types being presented to us.
    try:
        max_session_length = int(max_session_length_setting)
    except (TypeError, ValueError):
        # We got a response that doesn't look like a number; use the default.
        max_session_length = None

    # Get the session expiration length based on the maximum session length
    # setting, combined with any session length received from the backend.
    session_expiry = get_session_timeout(
        social_user,
        enable_session_expiration=enable_session_expiration,
        max_session_length=max_session_length,
    )

    try:
        # Set the session length to our previously determined expiry length.
        backend.strategy.request.session.set_expiry(session_expiry)
    except OverflowError:
        # The timestamp we used wasn't in the range of values supported by
        # Django for session length; use the platform default. We tried.
        backend.strategy.request.session.set_expiry(DEFAULT_SESSION_TIMEOUT)
~~~

## 実際のランディング処理 social_core.actions.do_complete

- [social_core.actions.do_complete](https://github.com/python-social-auth/social-core/blob/master/social_core/actions.py#L30)

~~~py
def do_complete(
    backend,              # バックエンド(Facebook, Google, Amazon...)
    login,                # ログイン処理ロジック関数
    user=None,            # リクエストユーザー
    redirect_name='next', # リダイレクトが必要な場合の戻りのクエリの指定
    *args, **kwargs
):
    data = backend.strategy.request_data()          #

    is_authenticated = user_is_authenticated(user)  # ログインしている？
    user = user if is_authenticated else None       # ログインユーザー

    # パーシャルデータ復元
    partial = partial_pipeline_data(backend, user, *args, **kwargs)
    if partial:
        # パーシャルがあったら
        user = backend.continue_pipeline(partial)
    else:
        # # パーシャルがないので完了
        user = backend.complete(user=user, *args, **kwargs)

    # 以降、ユーザーに対してのUI分岐処理

    # セッションからリダイレクト情報を取得する   
    # pop redirect value before the session is trashed on login(),
    # but after the pipeline
    # so that the pipeline can change the redirect if needed
    redirect_value = \
        backend.strategy.session_get(redirect_name, '') or \
        data.get(redirect_name, '')

    # ユーザーのモデル確認
    # check if the output value is something else than a user and just
    # return it to the client
    user_model = backend.strategy.storage.user.user_model()
    if user and not isinstance(user, user_model):
        return user

    # ここより先は 1) ユーザーのログイン(認証クッキー紐付け) 2)次のリダイレクト先を決定

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
            # ログインさせる
            login(backend, user, social_user)
            # store last login backend name in session
            backend.strategy.session_set('social_auth_last_login_backend',
                                         social_user.provider)

            if is_new:
                # 新規ユーザー
                url = setting_url(backend,
                                  'NEW_USER_REDIRECT_URL',
                                  redirect_value,
                                  'LOGIN_REDIRECT_URL')
            else:
                # 登録済みユーザー
                url = setting_url(backend, redirect_value,
                                  'LOGIN_REDIRECT_URL')
        else:
            # 無効なユーザー
            if backend.setting('INACTIVE_USER_LOGIN', False):
                social_user = user.social_user
                # ログインさせる
                login(backend, user, social_user)
            url = setting_url(backend, 'INACTIVE_USER_URL', 'LOGIN_ERROR_URL',
                              'LOGIN_URL')
    else:
        # エラー
        url = setting_url(backend, 'LOGIN_ERROR_URL', 'LOGIN_URL')

    if redirect_value and redirect_value != url:
        redirect_value = quote(redirect_value)
        url += ('&' if '?' in url else '?') + \
               '{0}={1}'.format(redirect_name, redirect_value)

    # URLの検証
    if backend.setting('SANITIZE_REDIRECTS', True):
        allowed_hosts = backend.setting('ALLOWED_REDIRECT_HOSTS', []) + \
                        [backend.strategy.request_host()]
        url = sanitize_redirect(allowed_hosts, url) or \
              backend.setting('LOGIN_REDIRECT_URL')

    # リダイレクトさせる
    return backend.strategy.redirect(url)
~~~

## OAuth2(Amazon...) でのランディング処理

### complete

- [social_core.backends.base.BaseAuth.complete](https://github.com/python-social-auth/social-core/blob/master/social_core/backends/base.py#L39)

~~~py
def complete(self, user=None, request=None, *args, **kwargs):  # django
    ''' def complete(self, *args, **kwargs):
    '''
    return self.auth_complete(*args, **kwargs)
~~~

### auth_complete

- [social_core.backends.oauth.BaseOAuth2.auth_complete](https://github.com/python-social-auth/social-core/blob/master/social_core/backends/oauth.py#L385)

~~~py
@handle_http_errors
def auth_complete(self, user=None, request=None, *args, **kwargs):
# def auth_complete(self, *args, **kwargs):
    """Completes login process, must return user instance"""
    self.process_error(self.data)     # エラー判定
    state = self.validate_state()     # state パラメータ判定

    # アクセストークンの取得(Code Flow)
    response = self.request_access_token(
        self.access_token_url(),
        data=self.auth_complete_params(state),
        headers=self.auth_headers(),
        auth=self.auth_complete_credentials(),
        method=self.ACCESS_TOKEN_METHOD
    )

    # アクセストークン応答の処理
    self.process_error(response)

    return self.do_auth(
        response['access_token'], response=response, *args, **kwargs)
~~~                        

~~~py
@handle_http_errors
# def do_auth(self, access_token, *args, **kwargs):
def do_auth(self, access_token, user=None, request=None, *args, **kwargs):
    """Finish the auth process once the access_token was retrieved"""

    # JSONからユーザーデータを取得
    data = self.user_data(access_token, *args, **kwargs)
    response = kwargs.get('response') or {}   # ユーザーデータ応答
    response.update(data or {})

    # ユーザーデータにアクセストークン(必要であれば)をマージ
    if 'access_token' not in response:
        response['access_token'] = access_token

    # user,  request, respose(ユーザーデータ), backendで authenticateを呼ぶ
    kwargs.update({'response': response, 'backend': self})
    return self.strategy.authenticate(*args, **kwargs)    # django authenticate
~~~

### strategy.authenticate (Django)

- [social_django.strategy.DjangoStrategy.authenticate](https://github.com/python-social-auth/social-app-django/blob/master/social_django/strategy.py#L103)

~~~py
from django.contrib.auth import authenticate


# def authenticate(self, backend, *args, **kwargs):
def authenticate(
    self,
    backend,
    user=None,
    request=None,
    response=None,
    backend=None,
    *args, **kwargs
):
    kwargs['strategy'] = self
    kwargs['storage'] = self.storage
    kwargs['backend'] = backend
    return authenticate(*args, **kwargs)      # django API: Userを返します
~~~    

- [django.contrib.auth.authenticate](https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.authenticate)
- [source](https://docs.djangoproject.com/en/2.0/_modules/django/contrib/auth/#authenticate)

~~~py
def authenticate(request=None, **credentials):
    """
    If the given credentials are valid, return a User object.
    """
    for backend, backend_path in _get_backends(return_tuples=True):
        try:
            user = _authenticate_with_backend(backend, backend_path, request, credentials)
        except PermissionDenied:
            # This backend says to stop in our tracks - this user should not be allowed in at all.
            break
        if user is None:
            continue
        # Annotate the user object with the path of the backend.
        user.backend = backend_path
        return user

    # The credentials supplied are invalid to all backends, fire signal
    user_login_failed.send(sender=__name__, credentials=_clean_credentials(credentials), request=request)
~~~

~~~py
def _authenticate_with_backend(backend, backend_path, request, credentials):
    credentials = credentials.copy()  # Prevent a mutation from propagating.
    args = (request,)
    # Does the backend accept a request argument?
    try:
        inspect.getcallargs(backend.authenticate, request, **credentials)
    except TypeError:
        args = ()
        credentials.pop('request', None)
        # Does the backend accept a request keyword argument?
        try:
            inspect.getcallargs(backend.authenticate, request=request, **credentials)
        except TypeError:
            # Does the backend accept credentials without request?
            try:
                inspect.getcallargs(backend.authenticate, **credentials)
            except TypeError:
                # This backend doesn't accept these credentials as arguments. Try the next one.
                return None
            else:
                warnings.warn(
                    "Update %s.authenticate() to accept a positional "
                    "`request` argument." % backend_path,
                    RemovedInDjango21Warning
                )
        else:
            credentials['request'] = request
            warnings.warn(
                "In %s.authenticate(), move the `request` keyword argument "
                "to the first positional argument." % backend_path,
                RemovedInDjango21Warning
            )
    return backend.authenticate(*args, **credentials)
~~~

### backend.authenticate

- [social_core.backends.base.BaseAuth.authenticate](https://github.com/python-social-auth/social-core/blob/master/social_core/backends/base.py#L59)

~~~py
def authenticate(self, *args, **kwargs):
     """Authenticate user using social credentials
     Authentication is made if this is the correct backend, backend
     verification is made by kwargs inspection for current backend
     name presence.
     """
     # Validate backend and arguments. Require that the Social Auth
     # response be passed in as a keyword argument, to make sure we
     # don't match the username/password calling conventions of
     # authenticate.
     if 'backend' not in kwargs or kwargs['backend'].name != self.name or \
        'strategy' not in kwargs or 'response' not in kwargs:
         return None

     self.strategy = kwargs.get('strategy') or self.strategy
     self.redirect_uri = kwargs.get('redirect_uri') or self.redirect_uri
     self.data = self.strategy.request_data()
     kwargs.setdefault('is_new', False)

     pipeline = self.strategy.get_pipeline(self)      # パイプラインを取得
     args, kwargs = self.strategy.clean_authenticate_args(*args, **kwargs)
     return self.pipeline(pipeline, *args, **kwargs)  # パイプラインを実行(最終的にUserを返す)
~~~
