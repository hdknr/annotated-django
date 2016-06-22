- https://github.com/toml-lang/toml
- [pytoml](https://github.com/avakar/pytoml)
- [toml 0.7.0](https://pypi.python.org/pypi/toml/0.7.0) / https://github.com/uiri/toml
- [【個人メモ】設定ファイルフォーマットにはTOMLがいいのかも](http://qiita.com/futoase/items/fd697a708fcbcee104de)

~~~bash
$ cat .dein.toml

[[plugins]]
repo = 'Shougo/dein.vim'

[[plugins]]
repo = 'Shougo/vimproc'

  [plugins.build]
  windows = 'tools\\update-dll-mingw'
  cygwin  = 'make -f make_cygwin.mak'
  mac     = 'make -f make_mac.mak'
  linux   = 'make'
  unix    = 'gmake'

[[plugins]]
repo = 'Shougo/neosnippet-snippets'

~~~
~~~py
In [1]: import toml

In [2]: toml.loads(open('.dein.toml').read())
Out[2]:
{'plugins': [{'repo': 'Shougo/dein.vim'},
  {'build': {'cygwin': 'make -f make_cygwin.mak',
    'linux': 'make',
    'mac': 'make -f make_mac.mak',
    'unix': 'gmake',
    'windows': 'tools\\\\update-dll-mingw'},
   'repo': 'Shougo/vimproc'},
  {'repo': 'Shougo/neosnippet-snippets'}]}

In [3]: type(_)
Out[3]: dict
~~~

~~~py
In [6]: import yaml
In [8]: print yaml.dump(t)
plugins:
- {repo: Shougo/dein.vim}
- build: {cygwin: make -f make_cygwin.mak, linux: make, mac: make -f make_mac.mak,
    unix: gmake, windows: tools\\update-dll-mingw}
  repo: Shougo/vimproc
- {repo: Shougo/neosnippet-snippets}
~~~
