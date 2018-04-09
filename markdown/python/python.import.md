## pydoc.locate()

- [pydoc.py](https://github.com/python/cpython/blob/3.6/Lib/pydoc.py#L1576)

~~~py
>>> import  pydoc
>>> pydoc.__file__
'/home/vagrant/.anyenv/envs/pyenv/versions/2.7.9/lib/python2.7/pydoc.pyc'

>>> pydoc.locate('emailqueue.models.Server')
<class 'emailqueue.models.Server'>
~~~


## import_module

- [importlib.import_module](https://github.com/python/cpython/blob/3.6/Lib/importlib/__init__.py#L108)

~~~py
from importlib import import_module
import_module('alumni.defs')
~~~
