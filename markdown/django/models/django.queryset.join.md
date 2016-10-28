## LEFT OUTER JOIN

- [Annotating a Django queryset with a left outer join?](http://stackoverflow.com/questions/6500066/annotating-a-django-queryset-with-a-left-outer-join)

~~~py
class User(models.Model):
    name = models.CharField()

class EarnedPoints(models.Model):
    user = models.ForgeinKey(User)
    points = models.PositiveIntegerField()
~~~    

~~~py
users_with_points = User.objects.annotate(points=Sum("earned_points__points"))
~~~

~~~py
users_with_nopoints = User.objects.exclude(pk__in=users_with_points)
~~~

~~~py
users = users_with_points | users_with_nopoints
~~~
