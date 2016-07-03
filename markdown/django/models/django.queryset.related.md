## prefetch_related

- [Djangoでprefetch_relatedを便利に使う](http://qiita.com/shunsukeaihara/items/eaaace97f6db75355f95)


- 指定した app_label配下のモデルへのパーミッションを持つグループの一覧

~~~py
from django.db.models.query import Prefetch                                      

# Permission を app_labelで絞っておく
prefetch = Prefetch(                                                        
    'permissions',                                                          
    queryset=auth_models.Permission.objects.filter(                         
        content_type__app_label=app_label))                                 

# app_labelのパーミッションを持つグループ一覧
groups = auth_models.Group.objects.filter(                                  
    permissions__content_type__app_label=app_label                          
).prefetch_related(prefetch).distinct()      
~~~


## JOIN

- [Performing raw SQL queries](https://docs.djangoproject.com/ja/1.9/topics/db/sql/)
- [inner join between tables no related django](http://stackoverflow.com/questions/24347770/inner-join-between-tables-no-related-django)
- [Django-queryset join without foreignkey](http://stackoverflow.com/questions/19590483/django-queryset-join-without-foreignkey)

- [simonw/django-queryset-transform](https://github.com/simonw/django-queryset-transform)
