## 一覧に戻す

~~~html
{% for instance in object_list %}
  ....
  <a href="{% url 'blogs_edit' id=instance.id %}?next={{ request.get_full_path|urlencode }}"> 編集 </a>
  ....
{% endfor %}
~~~


~~~~html
<form ....>
{% bootstrap_form form layout="horizontal"  %}
{% buttons submit=_('Update') reset=_('Cancel')  %}
{% endbuttons %}
</form>

<script>
  $(function(){
    $("button[type=reset]").click(function(){
      window.location.href = "{% if request.GET.next %}{{ request.GET.next }}{% else %}{% url 'blogs_index' %}{% endif %}";
    });
  });
</script>

~~~

## メールにURLを添付する

- メールの本文をテンプレートにしてレンダリングする
- 登録後確認メールの例
- テンプレート変数: `user`(登録ユーザー), `request` (リクエスト)
- `request` は None の場合がある(コマンドで実行とか)

~~~
{% extends 'accounts/mails/layout.html' %}    {# HTMLメールで送る #}
{% load corekit %}                    {# user_token, current_site #}

{% block content %}
{% user_token user as tokens %}       
{% current_site request as site %}  

<a href="{{ request.scheme|default:'https' }}://{{ site.domain }}{% url 'accounts_profile_join' uidb64=tokens.uidb64 token=tokens.token %}">
  クリックして、パスワードを変更してください。
</a>

{% endblock %}
~~~


- templatetags/corekit.py

~~~py
from django import template
register = template.Library()


@register.simple_tag
def current_site(request):
    from django.contrib.sites.shortcuts import get_current_site
    return get_current_site(request)

@register.simple_tag
def user_token(user):
    # https://github.com/hdknr/django-corekit/blob/master/lib/corekit/auth/__init__.py#L29
    return auth.create_user_token(user)    
~~~
