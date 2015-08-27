バリデーション
-------------

- :ref:`django.core.validators.RegexValidator`
- モデルフォームはモデルの方に設定することもできる

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
