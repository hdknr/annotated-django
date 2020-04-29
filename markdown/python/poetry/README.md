# poetry

## Install

~~~bash
$ pip install poetry
~~~

## 開始

~~~bash
$ poetry new --name gpress django-gpress
Created package gpress in django-gpress
~~~

~~~bash
$ tree .
.
└── django-gpress
    ├── README.rst
    ├── gpress
    │   └── __init__.py
    ├── pyproject.toml
    └── tests
        ├── __init__.py
        └── test_gpress.py

3 directories, 5 files
~~~

## [add](https://python-poetry.org/docs/cli/#add)

PYPI:

~~~bash
$ poetry add djangorestframework
~~~

github url:

~~~bash
$ poetry add git+https://github.com/philipn/django-rest-framework-filters.git
~~~