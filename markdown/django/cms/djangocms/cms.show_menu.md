## show_menu


base.html:


~~~html

{% load menu_tags %}

.....

<div class="navbar-collapse collapse">
    <ul class="nav navbar-nav">
        {% show_menu 0 1 100 100 "menu.html" %}
    </ul>
</div>
~~~


### menu.html

~~~html
% load i18n menu_tags cache %}

{% for child in children %}
    <li class="{% if child.ancestor %}ancestor{% endif %}
        {% if child.selected %} active{% endif %}
        {% if child.children %} dropdown{% endif %}">
        {% if child.children %}
            <a class="dropdown-toggle" data-toggle="dropdown" href="#">
                {{ child.get_menu_title }} <span class="caret"></span>
            </a>
            <ul class="dropdown-menu">
                {% show_menu from_level to_level extra_inactive extra_active template "" "" child %}
            </ul>
        {% else %}
            <a href="{{ child.get_absolute_url }}"><span>{{ child.get_menu_title }}</span></a>
        {% endif %}
    </li>
    {% if class and forloop.last and not forloop.parentloop
~~~
