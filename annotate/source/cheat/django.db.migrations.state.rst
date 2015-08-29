django.db.migrations.state.InvalidBasesError
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- マイグレーションがあるモデルを継承しているモデルに
  マイグレーションがない場合に発生する。

::

    django.db.migrations.state.InvalidBasesError: 

    Cannot resolve bases for [
        <ModelState: 'circles.CircleLetter'>,
        <ModelState: 'alumni.Profile'>,
        <ModelState: 'alumni.Alumnus'>,
        <ModelState: 'alumni.Letter'>
    ]

    This can happen if you are inheriting models 
    from an app with migrations (e.g. contrib.auth)
    in an app with no migrations; 

    see https://docs.djangoproject.com/en/1.8/topics/migrations/#dependencies for more

.. code-block:: python

    class BaseModel(models.Model):
        ...

    class MailAddress(BaseModel):    
        ...

    class Mail(BaseModel):          
        ...

.. code-block:: python

    class CircleLetter(Mail):                                                           
        ...

.. code-block:: python

    class Profile(MailAddress):  
        ...

    class Alumnus(Profile): 
        ...

    class Letter(Mail):
        ... 

対処
~~~~~~~

- 継承している側のモデルのアプリケーションを INSTALLED_APPS からはずして
  マイグレーションさせて、そのあとでINSTALLED_APPSに戻す。

