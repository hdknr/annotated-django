[How can I generate a url to a particular item in the Django Admin Site from a view?](http://stackoverflow.com/questions/8057722/how-can-i-generate-a-url-to-a-particular-item-in-the-django-admin-site-from-a-vi)


## admin_change_url


~~~py
object_change_url = reverse('admin:myapp_mymodel_change', args=(obj.id,))
~~~

~~~html
{% url 'admin:myapp_mymodel_change' obj.id %}
~~~

~~~html
{% load admin_urls %}
{% url obj|admin_urlname:'change' obj.id %}"
~~~
