# 親モデルに応じてインラインの選択肢を絞る

## models.py

- 複数の路線の乗り換え駅になっている駅が地域に存在する

~~~py

class Region(BaseModel):
  ''' 地域 '''
  ....

class Line(BaseModel):
  ''' 路線 '''
  region = models.ForeignKey(Region)
  ...

class Station(BaseModel):
  ''' 駅 '''
  region = models.ForeignKey(Region)
  ...

class LineStation(BaseModel):
  ''' 停車駅 '''
  line = models.ForeignKey(Line)
  station = models.ForeignKey(Station)
  ....
~~~


## admin.py

- LineStation のインライン定義
- `get_formset()` をオーバーライド
- obj(Line) のインスタンスを formset.form に持たせる

~~~py
class LineStationAdminInline(admin.TabularInline):
    model = models.LineStation
    form = LineStationAdminInlineForm

    def get_formset(self, request, obj=None, **kwargs):
        res = super(
            LineStationAdminInline,
            self).get_formset(request, obj=None, **kwargs)

        # Lineインスタンスをフォームクラスに持たせる
        res.form.line = obj
        return res
~~~

- LineStationのフォーム
- LineStationのインラインでフォームにLineのインスタンスがセットされているはず
- `station` を Line.region に含まれるもののみに絞る

~~~py
class LineStationAdminInlineForm(forms.ModelForm):
    class Meta:
        model = models.LineStation

    def __init__(self, *args, **kwargs):
        if 'station' in self.base_fields and self.line:
            # Region中の Stationのみに限定する
            self.base_fields['station'].queryset = \
                self.line.region.station_set
        super(LineStationAdminInlineForm,
              self).__init__(*args, **kwargs)
~~~

## 複数ある場合

~~~py

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        exclude = []

    def __init__(self, *args, **kwargs):
        super(PackageForm, self).__init__(*args, **kwargs)

        # (4) 既存インスタンスの対応
        tariff = ('instance' in kwargs) and getattr(
            kwargs['instance'], 'tariff', None) or None
        if tariff:
            self.patch_tariff(self, tariff)

    @classmethod
    def patch_tariff(cls, form, tariff):
        # (0) フォームのリレーション条件を絞る処理 の実装
        qs = form.fields['mixes'].queryset.filter(tariff=tariff)
        form.fields['mixes'].queryset = qs

        qs = form.fields['delegate_to'].queryset.filter(tariff=tariff)
        form.fields['delegate_to'].queryset = qs
        return form


class PackageInlineFormSet(forms.models.BaseInlineFormSet):
    model = Package

    def __init__(self, *args, **kwargs):
        # (3) リクエストからインスタンスを取得する
        self.current_shipping = hasattr(self, 'request') \
            and getattr(self.request, '_current_shipping', None) or None
        super(PackageInlineFormSet, self).__init__(*args, **kwargs)

    @property
    def empty_form(self):
        # (4) 新規追加初期フォームの対応
        form = super(PackageInlineFormSet, self).empty_form
        return self.current_shipping and \
            form.patch_tariff(form, self.current_shipping) or form


class PackageInline(admin.TabularInline, app_admin.Mixin):
    model = Package
    form = PackageForm
    formset = PackageInlineFormSet

    def get_formset(self, request, obj=None, **kwargs):
        formset = super(PackageInline, self).get_formset(request, obj, **kwargs)
        formset.request = request # (2) request をフォームセットに渡す
        return formset


@admin.register(models.Tariff)
class TariffAdmin(admin.ModelAdmin):
    inlines = [PackageInline]

    def _create_formsets(self, request, obj, change):
        setattr(request, '_current_shipping', obj)  # (1) 値をリクエストに設定する
        return super(TariffAdmin, self)._create_formsets(
            request, obj, change        
~~~

## 親の属性を引き継ぐ

親モデルインスタンスの `plan` 属性をインラインのインスタンスに自動的に引き継ぐ

~~~py
from . import forms

class PlanPackageInline(admin.TabularInline):
    model = models.PlanPackage
    # readonly_fields = ['plan']             # NG: readonlyにしてしまうと、値がセットされない
    readonly_fields = ['plan_info']          # OK: 表示用のメソッドを使う
    exclude = []
    extra = 0
    formset = forms.PlanPackageFormSet       # フォームセット
    form = forms.PlanPackageForm             # フォーム

    def plan_info(self, obj):
        return obj.plan
~~~

- フォームセットが[新規フォームを作成](https://github.com/hdknr/annotated-django/commit/552d3ff203dc6f2852729d1823ebab2be8487b449)
- この時に、[get_form_kwargs で返される値](https://github.com/hdknr/annotated-django/commit/d1593ecdcded5c87b1acfbe3f235c802a6ba9ed7) がフォームの初期化に使われる
- 実際は `__init__` で作られる [form_kwargs](https://github.com/hdknr/annotated-django/commit/a2926851b7b666601e3a5ea9fa95661b567e180f) が複製される

~~~py
class PlanPackageFormSet(forms.models.BaseInlineFormSet):

    def patch_initial(self):
        ''' form_kwargs['initial'] を変更する '''

        initial = self.form_kwargs.get('initial', {})

        if hasattr(self.instance, 'plan'):
            # 初期値として plan を設定する
            initial['plan'] = self.instance.plan

        self.form_kwargs['initial'] = initial

    def __init__(self, *args, **kwargs):
        super(PlanPackageFormSet, self).__init__(*args, **kwargs)
        self.patch_initial()


class PlanPackageForm(forms.ModelForm):

    class Meta:
        model = models.PlanPackage
        exclude = []
        # plan は編集させない
        widgets = {
            'plan': forms.HiddenInput(), }
~~~