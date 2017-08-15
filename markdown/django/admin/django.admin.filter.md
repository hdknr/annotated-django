Admin の検索条件を ビューに渡す


# change_list.html

- Admin changelist の 現在の検索(query)をURLに渡す

~~~html
<a href="{% url communities_member_download %}?{{ request.GET.urlencode }}">メンバーのダウンロード</a>
~~~


# view

- `GET` を 辞書化して、 `filter` に名つきパラメータとして渡す

~~~py

def member_download(request):
    qs = models.Member.objects.filter(**request.GET.dict())
    ...
    return download_querset(qs)
~~~
