テンプレート

- [templates](http://docs.django-cms.org/en/release-3.4.x/introduction/templates_placeholders.html#templates)


~~~bash
$ tree mysite/templates/

mysite/templates/
├── base.html
├── fullwidth.html
├── sidebar_left.html
└── sidebar_right.html

0 directories, 4 files
~~~

## settings.CMS_TEMPLATES

~~~py
In [2]: from django.conf import settings

In [3]: settings.CMS_TEMPLATES
Out[3]:
(('fullwidth.html', 'Fullwidth'),
 ('sidebar_left.html', 'Sidebar Left'),
 ('sidebar_right.html', 'Sidebar Right'))
~~~

## base.html

~~~html
{% load cms_tags menu_tags sekizai_tags %}
<!doctype html>
<html>
    <head>
        <title>{% block title %}This is my new project home page{% endblock title %}</title>
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <style type="text/css">
            .nav {
                padding-left: 0;
            }
            .nav li {
                display: inline;
                list-style-type: none;
                padding-right: 20px;
            }
            .container {
                width: 940px;
                margin: 0 auto
            }
            .content {
                float: left;
                width: 80%;
            }
            .sidebar {
                float: left;
                width: 20%;
            }
        </style>
        {% render_block "css" %}
    </head>
    <body>
        {% cms_toolbar %}
        <div class="container">
            <ul class="nav">
                {% show_menu 0 100 100 100 %}
            </ul>
            {% block content %}{% endblock content %}
        </div>
        {% render_block "js" %}
    </body>
</html>
~~~

## fullwidth.html

~~~html
{% extends "base.html" %}
{% load cms_tags %}

{% block title %}{% page_attribute "page_title" %}{% endblock title %}

{% block content %}
	{% placeholder "content" %}
{% endblock content %}
~~~

## sidebar_left.html

~~~html
{% extends "base.html" %}
{% load cms_tags %}

{% block title %}{% page_attribute "page_title" %}{% endblock title %}

{% block content %}
    <div class="sidebar">
        {% placeholder "sidebar" %}
    </div>
    <div class="content">
        {% placeholder "content" %}
    </div>
{% endblock content %}
~~~

## sidebar_right.html

~~~html
{% extends "base.html" %}
{% load cms_tags %}

{% block title %}{% page_attribute "page_title" %}{% endblock title %}

{% block content %}
    <div class="content">
        {% placeholder "content" %}
    </div>
    <div class="sidebar">
        {% placeholder "sidebar" %}
    </div>
{% endblock content %}
~~~

## CMS_TEMPLATE 変数

- [CMS_TEMPLATE](http://docs.django-cms.org/en/release-3.4.x/how_to/templates.html#cms-template)
- ページに設置されているテンプレート
- `extends` の切り替えに使える

~~~html
{% extends CMS_TEMPLATE %}
{% load cms_tags %}
{% block main %}
{% for item in object_list %}
    {{ item }}
{% endfor %}
{% static_placeholder "sidebar" %}
{% endblock main %}
~~~
