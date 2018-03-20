## Shift_JISでPOSTする

~~~py
def request_data(instance):
    '''モデルをdictに変換'''
    from django.forms.models import model_to_dict
    return model_to_dict(instancd, exclude=['id',])

def request_data_encoded(instance, encoding='utf-8'):
    '''dictを x-www-form-urlencoded シリアライズする'''
    import urllib
    return urllib.parse.urlencode(
        self.request_data, encoding=encoding)

def request_headers(header={}, encoding='utf-8'):
    '''リクエストヘッダ'''
    ret = {
        'Content-Type': f"application/x-www-form-urlencoded; charset={encoding}",
    }
    ret.update(header)
    return ret

def call_shift_jis(endpoint, instance):
    '''SHIFT_JISでデータを送信する'''
    encoding = 'Shift_JIS'
    res = requests.post(
        endpoint,
        headers=request_headers(encoding=encoding),
        data=self.request_data_encoded(instance, encoding=encoding)
    )
    res.encoding = res.apparent_encoding      # 戻りのエンコーディングに注意
    return res
~~~
