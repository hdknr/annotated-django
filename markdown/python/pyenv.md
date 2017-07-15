## anyenv - install

~/bin/setup/anyenv.bash:

~~~bash
#!/bin/bash
PKGS=(
    build-essential
    curl
    libbz2-dev
    libreadline-dev
    libsqlite3-dev
    libssl-dev
    llvm
    make
    wget
    zlib1g-dev
)

sudo apt-get update && sudo apt-get install -y  "${PKGS[@]}"
git clone https://github.com/riywo/anyenv ~/.anyenv
~~~

~~~
$ ~/bin/setup/anyenv.bash
~~~

~/bin/env/anyenv.bash:

~~~bash
export PATH="$HOME/.anyenv/bin:$PATH"
eval "$(anyenv init -)"

for D in `\ls $HOME/.anyenv/envs`; do
    export PATH="$HOME/.anyenv/envs/$D/shims:$PATH"
done
~~~

~~~
$ source ~/bin/env/anyenv.bash
~~~

## list env

~~~
$ anyenv install -l
Available **envs:
  denv
  goenv
  jenv
  luaenv
  ndenv
  phpenv
  plenv
  pyenv
  rbenv
  scalaenv
~~~

~/bin/setup/pyenv.bash:

~~~bash
#/bin/bash
# https://github.com/pyenv/pyenv-installer
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
git clone https://github.com/yyuu/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
~~~


## pyenv: error: failed to download Python-2.7.10.tgz

- OSが古いとエラーになる

~~~
$ pyenv install 2.7.10
Downloading Python-2.7.10.tgz...
-> https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tgz
error: failed to download Python-2.7.10.tgz

BUILD FAILED (Ubuntu 8.04 using python-build 20150601-6-g22ecefd)
~~~

~~~
$ export PYTHON_BUILD_MIRROR_URL="http://yyuu.github.io/pythons"
~~~

## pyenv global とかで切り替わらない

- `~/.python-version` が存在する

~~~bash
$ rm -rf .python-version
~~~


# 記事

- [Rubyist が pyenv を使うときに知っておいてほしいこと](http://qiita.com/methane/items/5afdabd513a18049c34f)
