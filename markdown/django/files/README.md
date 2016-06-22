Django Files

- [The File object](https://docs.djangoproject.com/ja/1.9/ref/files/file/)

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

- [指定された条件のレコードをExcelでダウンロードする](django.openpyxl.md)
