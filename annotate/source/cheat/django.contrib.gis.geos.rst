インストール
---------------

- `GeoDjango Installation <https://docs.djangoproject.com/en/1.8/ref/contrib/gis/install/>`_

.. code-block:: bash

    $ sudo apt-get install binutils libproj-dev gdal-bin libgdal1-dev
    $ export CPLUS_INCLUDE_PATH=/usr/include/gdal
    $ export C_INCLUDE_PATH=/usr/include/gdal
    $ pip install GDAL==1.10.0
