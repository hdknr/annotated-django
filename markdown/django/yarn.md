Yarn

~~~
$ npm install -g yarn
~~~


# theme アプリ


~~~bash
$ python manage.py startapp theme
$ mkdir theme/yarn
$ cd theme/yarn
~~~~

- bootstrap

~~~bash
$ yarn add bootstrap
$ cat packages.json
~~~

~~~js
{
  "dependencies": {
    "bootstrap": "^3.3.7"
  }
}
~~~

## theme/static

`lib` シンボリックリンク

~~~bash
$ mkdir static
$ cd static
$ ln -s ../yarn/node_modules lib
~~~


# collectstatic

app/settings.py:

~~~py
######
INSTALLED_APPS += [
    'theme',
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
~~~

~~~bash
$ python manage.py collectstatic
~~~

# .gitignore

~~~~
# yarn
yarn.lock
node_modules

# django
web/static
~~~~
