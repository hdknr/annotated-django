## Cookbook

### クエリパラメータをアンカーに渡す

- django.core.context_processors.request が必要

setttings.py:

~~~py
TEMPLATES = [
    {   
        # ....
        'OPTIONS': {
            'context_processors': [
                # ....
                "django.template.context_processors.request",
            ],  
        },  
    },  
]

~~~

page/index.html:

~~~html
<a href="{% url 'page_detail' %}?{{ request.GET.urlencode }}">詳細</a>
~~~


### builtin:  `{% load %}` しなくてもタグ/フィルタを使う

- [BlockNode](https://github.com/django/django/blob/master/django/template/loader_tags.py#L41)
- [built-in backend](https://docs.djangoproject.com/en/1.9/topics/templates/#module-django.template.backends.django)

~~~py
OPTIONS={
    'builtins': ['myapp.builtins'],
}
~~~

### BlockNode

`{% block title %}` など

~~~py
In [1]: from django.template.loader import get_template
In [2]: from django.template.loader_tags import BlockNode
In [3]: blocks = [n for n in get_template('base.html').template if isinstance(n, BlockNode)]
In [4]: [i.name for i in blocks]
Out[4]: ['title', 'meta', 'style', 'favicon', 'content', 'local_template', 'bottom']
~~~
