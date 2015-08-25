.. code-block:: python

    >>> from django.utils._os import abspathu
    >>> abspathu('upload/')
    u'/home/vagrant/.anyenv/envs/pyenv/versions/wordpress/src/djuploader/sample/upload'
    >>> abspathu('/tmp/upload/')                                                                                                                                           
    '/tmp/upload'

.. code-block:: python

    >>> import os
    >>> os.getcwdu()
    u'/home/vagrant/.anyenv/envs/pyenv/versions/wordpress/src/djuploader/sample'

    >>> os.path.isabs('/tmp')
    True
    >>> os.path.isabs('tmp')
    False
