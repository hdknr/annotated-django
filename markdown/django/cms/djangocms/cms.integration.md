## pollsアプリの追加

django-cmsと依存関係の無い単純なDjangoアプリ

~~~bash
$ pip install -e git+https://github.com/divio/django-polls.git#egg=polls
Obtaining polls from git+https://github.com/divio/django-polls.git#egg=polls
  Cloning https://github.com/divio/django-polls.git to /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/src/polls
Installing collected packages: polls
  Running setup.py develop for polls
Successfully installed polls
~~~

settings.py:

~~~py
INSTALLED_APPS += [
    'polls',
]
~~~

### urls.py

デフォルト:

~~~py
urlpatterns += i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^', include('cms.urls')),
)
~~~

~~~py
urlpatterns += i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^', include('cms.urls')),
)
~~~

### 動かす

migrate:

~~~bash
$ python manage.py migrate polls
Operations to perform:
  Apply all migrations: polls
Running migrations:
  Applying polls.0001_initial... OK
~~~

admin UI:

- /ja/admin/polls/poll/
- 新規作成する


登録:

- /ja/polls/ 一覧
- /ja/polls/1/ フォーム
- /ja/polls/1/results/ 完了と結果


## polls アプリのレイアウトを django-cmsサイトに合わせる

base.html:

~~~bash
$ mkdir mysite2/templates/polls
$ vi mysite2/templates/polls/base.html
~~~

~~~html
{% extends 'base.html' %}  {# django-cms サイトの base を拡張 #}

{% block content %}        {# django-cms content ブロックを修正 #}
    {% block polls_content %} {# polls がレンダリングするブロック #}
    {% endblock %}
{% endblock %}
~~~


## polls のプラグイン化

- [プラグイン](cms.plugin.md)
