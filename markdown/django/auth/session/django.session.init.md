## セッションキーの生成

- [request.session にデータがない場合、sessionidクッキーを返さない](https://github.com/hdknr/annotated-django/commit/a7c60d43e241a043527f7f0aa74c91dd05134b9f)
- [Django: How to set sessionid cookie for AnonymousUser without using SESSION_SAVE_EVERY_REQUEST](https://stackoverflow.com/questions/14949783/django-how-to-set-sessionid-cookie-for-anonymoususer-without-using-session-save)


### ミドルウェアで生成

- [Middleware](https://docs.djangoproject.com/en/2.0/topics/http/middleware/)

~~~py
class AppMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        return self.process_response(request, response)

    def force_create_session(self, request):
        '''初回にセッションを強制的に作成

        'django.contrib.sessions.middleware.SessionMiddleware'　のあとに置くこと
        '''
        session = getattr(request, 'session', None)
        if session and not session.session_key:
            request.session['ipaddress'] = request.META.get('REMOTE_ADDR')
            request.session.save()

    def process_request(self, request):
        self.force_create_session(request)

    def process_response(self, request, response):
        return response
~~~

settings.py:

~~~py
MIDDLEWARE += ['app.middlwares.AppMiddleware']
~~~

## ビューで都度確認

- [python - Sometimes request.session.session_key is None - Stack Overflow](https://stackoverflow.com/questions/39181655/sometimes-request-session-session-key-is-none)

~~~py
if not request.session.session_key:
    request.session.save()
~~~
