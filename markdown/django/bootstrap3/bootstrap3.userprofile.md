ユーザー属性フォーム


## お名前だけを横並びにする

- `div.form-group div.row` の下に、 2つのフィールドを horizontal で入れる
- `show_label=False` で個別のレベルは表示させない

~~~html
{% load i18n bootstrap3 static %}
{% bootstrap_field form.zipcode layout='horizontal' field_class="dropdown col-md-8" %}
{% bootstrap_field form.prefecture layout='horizontal' field_class="dropdown col-md-8" %}
{% bootstrap_field form.city layout='horizontal' field_class="dropdown col-md-8" %}
{% bootstrap_field form.address layout='horizontal' field_class="dropdown col-md-8" %}
{% bootstrap_field form.building layout='horizontal' field_class="dropdown col-md-8" %}
{% bootstrap_field form.phone layout='horizontal' field_class="dropdown col-md-8" %}

  <div class="form-group">
    <label for="{{ form.family_name.auto_id }}" class="col-md-3 control-label">お名前(漢字)</label>
    <div class="col-md-8 row">
      {% bootstrap_field form.family_name layout='horizontal' field_class="dropdown" form_group_class="col-md-6" show_label=False %}
      {% bootstrap_field form.first_name layout='horizontal' field_class="dropdown" form_group_class="col-md-6" show_label=False %}
    </div>
  </div>

<div class="form-group">
    <label for="{{ form.family_kana.auto_id }}" class="col-md-3 control-label">お名前(ふりがな)</label>
    <div class="col-md-8 row">
    {% bootstrap_field form.family_kana layout='horizontal' field_class="dropdown" form_group_class="col-md-6" show_label=False %}
    {% bootstrap_field form.first_kana layout='horizontal' field_class="dropdown" form_group_class="col-md-6" show_label=False %}
  </div>
</div>
~~~

## 郵便番号の前に`〒` を入れる

- jQuery
- `zipcode` を `div.input-group` で `wrap` する
- `zipcode` の前に `span.input-group-addon`  を挿入する

~~~js
$("input#id_zipcode")
  .wrap('<div class="input-group"/>')
  .before('<span class="input-group-addon">〒</span>');
~~~
