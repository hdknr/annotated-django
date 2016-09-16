# 文字列を変換する

- [django templates, find string replace with other string](http://stackoverflow.com/questions/2185133/django-templates-find-string-replace-with-other-string)


~~~html
<td>{{ forum.title.split|join:'<br/>' }}</td>
~~~
