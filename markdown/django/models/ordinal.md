# 序数


## モデル

~~~py
# coding: utf-8
from django.db.models import Max
from corekit.methods import CoreModel


class Info(CoreModel):

    @property
    def is_desc(self):
        '''降順か？'''
        return '-ordinal' in self._meta.ordering

    @property
    def lowers(self):
        '''自分より小さい一覧'''
        model = self._meta.concrete_model
        return model.objects.filter(
            ordinal__lte=self.ordinal).exclude(id=self.id)

    @property
    def uppers(self):
        '''自分より大きい一覧'''
        model = self._meta.concrete_model
        return model.objects.filter(
            ordinal__gte=self.ordinal).exclude(id=self.id)

    def decrement(self):
        '''序数を下げる'''
        instance = self.lowers.last() if self.is_desc else self.lowsers.first()
        self.swap_position(instance)

    def increment(self):
        '''序数をあげる'''
        instance = self.uppers.first() if self.is_desc else self.uppers.last()
        self.swap_position(instance)

    def swap_position(self, instance):
        '''序数を取り替える'''
        if instance:
            o = instance.ordinal
            instance.ordinal = self.ordinal
            self.ordinal = o
            instance.save()
            self.save()

    def set_ordinal(self):
        if self.ordinal == 0:
            # 新規追加オブジェクトの場合、最大値 + 1 をセットする
            model = self._meta.concrete_model
            self.ordinal = model.objects.aggregate(
                Max('ordinal'))['ordinal__max'] or 0
            self.ordinal = self.ordinal + 1
~~~


## フォーム

~~~py
class InfoForm(forms.ModelForm):

    class Meta:
        model = models.Info
        fields = ['due_on', 'new_expired_on',
                  'content', 'url', 'ordinal', 'enabled']

    def save(self, *args, **kwargs):
        self.instance.set_ordinal()
        res = super(InfoForm, self).save(*args, **kwargs)
        return res
~~~


## ビュー

~~~py

class InfoView(core_views.View):

    @core_views.handler(
        url=r'^info$',
        name="pages_info_index", order=40,)
    def index(self, request):
        instances = filters.InfoFilter(request.GET or None)
        return self.render(
            'pages/info/index.html', instances=instances)

    @core_views.handler(
        url=r'^info/(?P<id>\d+)/move/(?P<to>[^/]+)$',
        name="pages_info_move", order=20,)
    def move(self, request, id, to):
        instance = models.Info.objects.filter(id=id).first()
        if instance:
            if to == 'up':
                instance.increment()
            elif to == 'down':
                instance.decrement()

        return self.index(request)
~~~    


## テンプレート

~~~html
{% for instance in object_list %}
  <tr>
    {% if perms.pages.add_info %}
      ....
      <td>{{ instance.ordinal }}
          <a href="{% url view.handlers.move id=instance.id to='up' %}?{{ request.GET.urlencode }}">{% trans 'Position Up' %}</a>
          <a href="{% url view.handlers.move id=instance.id to='down' %}?{{ request.GET.urlencode }}">{% trans 'Position Down' %}</a>
      </td>
    {% endif %}
  </tr>
{% endfor %}

~~~


## 再ナンバリング

~~~py
count = models.Info.objects.count()
for (i, obj) in enumerate(models.Info.objects.all()):
    obj.ordinal = count - i if obj.is_desc else i
    obj.save()
~~~    
