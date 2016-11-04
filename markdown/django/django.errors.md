エラー処理

## 取り込みデータ(CSV/Excel)にフォームをかませてバリデーションメッセージを記録する

~~~py
from django.http.request import QueryDict  
from . import forms, models
import json

def add_member(rowdata):
  # rowdata : dict, keyはモデルのフィールド名とする

  # 読み取りデータを使って既存のメンバーを探し、いなかったら新規作成
  member = community.member_set.find(**rowdata) or models.Member(                  
    community=community)       

  # QueryDict 化する
  data = QueryDict(mutable=True)                                               
  data.update(rowdata)  

  # フォーム設定
  form = forms.MemberImportForm(data, instance=member)    
  if form.is_valid():
      form.save()
  else:
      err = from_errordict(form.errors)
      record_error(json.dumps(
        {'data': rowdata, 'errors': err}, ensure_ascii=False, indent=2))
~~~

~~~py

def from_errorlist(errorlist):
    # ErrorList
    res = []
    for error in errorlist.as_data():
        res.append(u"{}[{}]".format(
            list(error)[0], error.code))
    return res


def from_errordict(errordict):
    # ErrorDict
    return {f: from_errorlist(e) for f, e in errordict.items()}
~~~  
