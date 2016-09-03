- [How to use GenericForeignKey in Django](https://axiacore.com/blog/how-use-genericforeignkey-django/)

~~~py
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Poll(models.Model):
    question = models.CharField(max_length=500)
    answers = # ...
    # ...
    limit = models.Q(app_label='miapp', model='page') | \
        models.Q(app_label='miapp', model='article')
    content_type = models.ForeignKey(
        ContentType,
        verbose_name=_('content page'),
        limit_choices_to=limit,
        null=True,
        blank=True,
    )
    object_id = models.PositiveIntegerField(
        verbose_name=_('related object'),
        null=True,
    )
    content_object = GenericForeignKey('content_type', 'object_id')
~~~    

- [AutocompleteGeneric, for GenericForeignKey or GenericManyToMany](https://django-autocomplete-light.readthedocs.io/en/1.4.9/generic.html)
