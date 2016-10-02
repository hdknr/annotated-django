## goods_id でカウントを取る

~~~
In [1]: from django.db.models import Count
In [3]: SupplierGoods.objects.all().values('goods_id').annotate(total=Count('goods_id')).order_by('total')
~~~

## 合計数が１以上

~~~
In [4]: SupplierGoods.objects.all().values('goods_id').annotate(total=Count('goods_id')).filter(total__gt=1)
Out[4]: <QuerySet []>
~~~
