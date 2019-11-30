# 乱数

## ランダム文字列

~~~py
import random
''.join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for i in range(6)])
~~~

~~~
'avvmtq'
~~~

時刻がわかるように:

~~~py
datetime.now().strftime('%Y%m%d%H%M%S%f') + ''.join([random.choice("abcdefghijklmnopqrstuvwxyz") for i in range(4)])
~~~
