# tox

- http://tox.readthedocs.io/en/latest/index.html

## django 2.1 の tox.ini

~~~ini
# Tox (https://tox.readthedocs.io/) 複数の virtualenvでテストを実行するツール。
# この設定ではサポートされている全バージョンのPythonでのテストスィートを実行させることができる。
# tox を使うためにはこのディレクトリで以下のコマンドを実行する。
#
#       $ pip install tox
#       $ tox

####################################################################################
# [tox] グローバルオプション

[tox]
# sdist を作らないようにします(大きすぎるので)
skipsdist = true

# [testenv:py3], [testenv:flake8], [testenv:docs], [testenv:isort] のvirtualenv がテストされます
# isort https://isort.readthedocs.io/en/stable/
envlist =
    py3
    flake8
    docs
    isort

####################################################################################
### virutalenv 'py3' の設定

[testenv:py3]
# virtualenvを作るのに python3 を使います
basepython = python3

####################################################################################
### テスト設定
[testenv]
# パッケージ(django 2.1)を setup.py develop でインストールします。
usedevelop = true

# ワイルドカード環境変数リスト。 toxが起動されたシェルから引き継がれる変数
passenv = DJANGO_SETTINGS_MODULE PYTHONPATH HOME DISPLAY

# テストプロセスに設定される環境変数
setenv =
    PYTHONDONTWRITEBYTECODE=1

# 依存パッケージ
deps =
    py{3,35,36,37}: -rtests/requirements/py3.txt
    postgres: -rtests/requirements/postgres.txt
    mysql: -rtests/requirements/mysql.txt
    oracle: -rtests/requirements/oracle.txt

# ワーキングディレクトリを `tests` にします 
changedir = tests

# テストで実行されるコマンド
# {posargs} は tox を起動した時に指定した引数
# {envpython} virtualenvのPythonインタプリタ
# http://tox.readthedocs.io/en/latest/config.html#substitutions-for-virtualenv-related-sections
commands =
    {envpython} runtests.py {posargs}


####################################################################################
# ここでは flake8 で 自動コードレビューします
# http://flake8.pycqa.org/en/latest/#

[testenv:flake8]
basepython = python3
usedevelop = false
deps = flake8
# tox.ini があるディレックトリです
changedir = {toxinidir}
commands = flake8 .


####################################################################################
# ここではドキュメントのスペルチェックをします
# http://sphinxcontrib-spelling.readthedocs.io/en/latest/run.html
[testenv:docs]
basepython = python3
usedevelop = false
# commandsで使われるコマンドを指定します(warningを抑制します)
whitelist_externals =
    make
deps =
    Sphinx
    pyenchant
    sphinxcontrib-spelling
changedir = docs
commands =
    make spelling


####################################################################################
[testenv:isort]
basepython = python3
usedevelop = false
deps = isort
changedir = {toxinidir}
commands = isort --recursive --check-only --diff django tests scripts

####################################################################################
# javascriptのテストをします
[testenv:javascript]
usedevelop = false
deps =
changedir = {toxinidir}
whitelist_externals = npm
commands =
    npm install
    npm test
~~~
