
- [staticファイル](./static/)
- [PDF](./pdf/)

## [django.core.files](django.core.files)

- 文字列をファイルに保存する

## 指定したディレクトリの以下にある画像ファイルをモデルデータに格納する

~~~py
from django.core.files import File
from xoops.models import XoopsActivity                              
import re

for path, _x, files in os.walk(base):                                       
    if _ or not files:                                                      
         continue                                                            
    match = re.search(r"(\d+)$", path)      # 活動 ID を取得                                  
    aid = match.group(1)                                                    

    activity = XoopsActivity.objects.get(aid=aid)                  
    activity = activity and activity.new_activity                       

    map(lambda img: activity.activityphoto_set.create(                  
          photo=File(open(os.path.join(path, img)))), files)                                                          
~~~

## Excel

openpyxl:

- [指定された条件のレコードをExcelでダウンロードする](django.openpyxl.md)

[pyexcel](pyexcel.md):

- TODO:



## ImageField

- [Django の ImageField](http://qiita.com/kojionilk/items/da20c732642ee7377a78)
