- [メニュー](cms.menus.md)

## {% show_menu %}


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

## show_menu パラメータ

### start_level

- デフォルト=0 (ルートノード)
- ルートが不要であれば、 `start_level=1` にする


### end_level

- デフォルト=100

### extra_inactive

- デフォルト=0 (ルートノード)
- 現在のノードの直接の先祖/子孫では無いノードのレベルがこの範囲で表示されない

### extra_active

- デフォルト=100
- 現在のノードの直接の先祖/子孫では無いノードのレベルがこの範囲で表示される

### namespace

- 使用するメニューのネームスペース
- 指定されないと全てのネームスペースが対象

### root_id

- ルートのID

### template

- テンプレート名



### menu.html

~~~html
{% load i18n menu_tags cache %}

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
    {% if class and forloop.last and not forloop.parentloop %}{% endif %}
{% endfor %}
~~~


child: ナビゲーションノード:


属性              | 　　内容
-----------------|-----------------------
is_leaf_node     | `=true` ツリーの末端
level            | レベル(0開始)
menu_level       | メニューのルートノードからのノードレベル
get_absolute_url | ノードのURL
title            | タイトル(現在の言語)
selected         | `=true` 現在選択されている
ancestor         | `=true` 現在のノードの先祖
sibling          | `=true` 現在のノードの兄弟
descendant       | `=true` 現在のノードの子孫
soft_root        | `=true` [ソフトルート](cms.menus.md)
