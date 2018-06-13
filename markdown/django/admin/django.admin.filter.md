## admin.SimpleListFilter

### 値がNone/ not Noneを探す

~~~py
from django.contrib import admin

class NoneListFilter(admin.SimpleListFilter):
    def lookups(self, request, model_admin):
        # 選択肢
        return (
            ('1', _('None'), ),         # None
            ('0', _('!= None'), ),      # not None
        )

    def queryset(self, request, queryset):
        # 検索
        if self.value() in ('0', '1'):
            kwargs = {
                '{0}__isnull'.format(self.parameter_name): self.value() == '1'
            }
            return queryset.filter(**kwargs)
        return queryset

    @classmethod
    def create(cls, title, parameter_name):
        # サブクラスを作る
        return type(
            'NoneListFilterEx', (cls, ),
            {'title': title, 'parameter_name': parameter_name})
~~~

~~~py
@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_filter = (
        'status',
        NoneListFilter.create(_('Attachment'), 'attachment'))       # 添付ファイルの有無で検索
~~~


## admin.RelatedFieldListFilter

### app_label + content_type の相関で検索

選択された `app_label` の `content_type` のみを選択肢として表示

~~~py
class CorelatedFilter(admin.RelatedFieldListFilter):

    def field_choices(self, field, request, model_admin):
        # 相関がある選択肢を返す
        name = "{}__{}".format(field.name, self.cofield)
        covalue = request.GET.get(name, '')
        if not covalue:
            return field.get_choices(include_blank=False)
        return field.get_choices(
            include_blank=False,
            limit_choices_to={self.cofield: covalue})

    @classmethod
    def create(cls, field, cofield):
        # サブクラスを作る
        return (
            field, 
            type('CorelatedFilterEx', (cls, ),
                 {'cofield': cofield}), )
~~~

~~~py
from django.contrib.auth.models import Permission

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_filter = [
        'content_type__app_label',
        CorelatedFilter.create('content_type', 'app_label')] 
~~~


## Admin の検索条件を ビューに渡す


### change_list.html

- Admin changelist の 現在の検索(query)をURLに渡す

~~~html
<a href="{% url communities_member_download %}?{{ request.GET.urlencode }}">メンバーのダウンロード</a>
~~~


### view

- `GET` を 辞書化して、 `filter` に名つきパラメータとして渡す

~~~py

def member_download(request):
    qs = models.Member.objects.filter(**request.GET.dict())
    ...
    return download_querset(qs)
~~~
