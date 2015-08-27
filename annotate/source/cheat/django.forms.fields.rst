バリデーション
-------------

- :ref:`django.core.validators.RegexValidator`

.. code-block:: python

    from django.core.validators import RegexValidator

    class OrderForm(forms.ModelForm):

        def __init__(self, *args, **kwargs):
            ....
            self.base_fields['phone'].required = True
            self.base_fields['phone'].validators = [
                RegexValidator(
                    regex=r'^[\d\-]{9,15}$',
                    message=_('Phone Number Validation'), )
            ]
            ....
            super(OrderForm, self).__init__(*args, **kwargs)

- モデルレベルで設定すればModelFormに引き継がれる

.. code-block:: python

    class Order(models.Model)
        phone = models.CharField(
          _('Phone Number'), help_text=_('Phone Number Help'),
          max_length=13,
          validators=[
              RegexValidator(
                  regex=r'^[\d\-]{9,15}$',
                  message=_('Phone Number Validation'), )],)
