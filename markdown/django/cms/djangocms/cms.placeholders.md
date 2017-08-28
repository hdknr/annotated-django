
- [placeholders](http://docs.django-cms.org/en/release-3.4.x/introduction/templates_placeholders.html#placeholders)

## placeholder テンプレートタグ


~~~~html
{% block content %}
	{% placeholder "content" %}
{% endblock content %}
~~~

![](cms.placeholders.before.png)


~~~html
{% block content %}
	{% placeholder "feature" %} 	{# HDKNR #}
	{% placeholder "content" %}
	{% placeholder "splashbox" %}	{# HDKNR #}
{% endblock content %}
~~~

![](cms.placeholders.after.png)

## static placeholder テンプレートタグ

- 一箇所変更すると全ページに反映される

base.html とかに置く:

~~~html
...
<body>
    {% cms_toolbar %}

    <div class="container">
        <ul class="nav">
            {% show_menu 0 100 100 100 %}
        </ul>
        {% block content %}{% endblock content %}
    </div>

    <footer>
      {% static_placeholder 'footer' %}
    </footer>

    {% render_block "js" %}
</body>
~~~
![](cms.placeholders.static.png)
