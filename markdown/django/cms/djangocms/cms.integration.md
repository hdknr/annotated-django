## urlconf


デフォルト:

~~~py
urlpatterns += i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^', include('cms.urls')),
)
~~~

`cms.urls` の前に追加:

~~~py
urlpatterns += i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^', include('cms.urls')),
)
~~~


## レイアウト

django-cmsのレイアウト `base.html` を継承する:

~~~html
{% extends 'base.html' %}

{% block content %}
    {% block polls_content %}
    {% endblock %}
{% endblock %}
~~~

## INSTALLED_APPS

INSTALLED_APPS に追加
