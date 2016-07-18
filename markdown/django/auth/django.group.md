## Admin: Groupからユーザーへのリンクを追加

- `templates/admin/auth/group/change_form.html`

~~~html

{% extends "admin/change_form.html" %}
{% load i18n static %}


{% block field_sets %}
 {{ block.super }}

<fieldset class="module aligned ">
    <h2>その他</h2>
    <div class="form-row field-remarks">
      <div>
        <label for="id_user">ユーザー数</label>
        <span id="id_user">
          <a href="{% url 'admin:auth_user_changelist' %}?groups__id__exact={{ original.id }}">
            {{ original.user_set.count }}</a></span>
        <p class="help">ユーザー数</p>
      </div>
    </div>
</fieldset>

{% endblock %}
~~~
