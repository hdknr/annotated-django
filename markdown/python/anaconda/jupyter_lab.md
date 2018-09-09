# Jupyter Lab

- [Jupyter Labの便利な新機能まとめ -機械学習エンジニアが愛する開発環境（IDE）の決定版](https://www.codexa.net/jupyter-lab-beta-review-ml-ide/)
- [jupyter](http://jupyter.org/)

## インストール

- [JupyterLabを触ってみた - Qiita](https://qiita.com/Miggy/items/0290ade68de6009b4ab9)

~~~bash 
$ pip install jupyterlab
~~~

~~~bash 
$ jupyter serverextension enable --py jupyterlab --sys-prefix
Enabling: jupyterlab
- Writing config: /Users/hide/.anyenv/envs/pyenv/versions/anaconda3-5.2.0/etc/jupyter
    - Validating...
      jupyterlab 0.32.1 OK
~~~

## Django

~~~bash 
$ DJANGO_SETTINGS_MODULE=app.settings jupyter lab --notebook-dir notebooks
~~~

## Plotly

- [Jupyter lab Plotlyを表示させる - python_analytics](https://python-analytics.hatenadiary.jp/entry/2018/06/30/112442)

~~~bash
$ jupyter labextension install @jupyterlab/plotly-extension

> /Users/hide/.anyenv/envs/ndenv/shims/npm pack @jupyterlab/plotly-extension
jupyterlab-plotly-extension-0.17.1.tgz

> node /Users/hide/.anyenv/envs/pyenv/versions/anaconda3-5.2.0/lib/python3.6/site-packages/jupyterlab/staging/yarn.js install
yarn install v1.5.1
info No lockfile found.
[1/4] 🔍  Resolving packages...
warning @jupyterlab/plotly-extension > plotly.js > mapbox-gl > @mapbox/gl-matrix@0.0.1: This
warning @jupyterlab/plotly-extension > plotly.js > gl-plot2d > gl-select-static > cwise > static-module > through2 > xtend > object-keys@0.4.0:
warning css-loader > cssnano > autoprefixer > browserslist@1.7.7: Browserslist 2 could fail on reading Browserslist >3.0 config used in other tools.
warning css-loader > cssnano > postcss-merge-rules > browserslist@1.7.7: Browserslist 2 could fail on reading Browserslist >3.0 config used in other tools.
warning css-loader > cssnano > postcss-merge-rules > caniuse-api > browserslist@1.7.7: Browserslist 2 could fail on reading Browserslist >3.0 config used in other tools.
[2/4] 🚚  Fetching packages...
[3/4] 🔗  Linking dependencies...
warning "@jupyterlab/json-extension > react-json-tree@0.10.9" has incorrect peer dependency "react@^15.0.0".
warning "@jupyterlab/json-extension > react-json-tree@0.10.9" has incorrect peer dependency "react-dom@^15.0.0".
warning "@jupyterlab/vdom-extension > @nteract/transform-vdom@1.1.1" has incorrect peer dependency "react@^15.6.1".
[4/4] 📃  Building fresh packages...
success Saved lockfile.
warning Your current version of Yarn is out of date. The latest version is "1.9.4", while you're on "1.5.1".
✨  Done in 83.76s.
> node /Users/hide/.anyenv/envs/pyenv/versions/anaconda3-5.2.0/lib/python3.6/site-packages/jupyterlab/staging/yarn.js run build:prod
yarn run v1.5.1
$ webpack --config webpack.prod.config.js
Hash: 789ecd1e53af2be17710
Version: webpack 2.7.0
Time: 59639ms
                                 Asset     Size  Chunks                    Chunk Names
        vendor.945719a65376e0552de5.js  1.57 MB       2  [emitted]  [big]  vendor
  912ec66d7572ff821749319396470bde.svg   444 kB          [emitted]  [big]
  674f50d287a8c48dc19ba404d20fe713.eot   166 kB          [emitted]
 fee66e712a8a08eef5805a46892932ad.woff    98 kB          [emitted]
af7ae505a9eed503f8b8e6982036873e.woff2  77.2 kB          [emitted]
             0.279ec850a9242db04c85.js   465 kB       0  [emitted]  [big]
          main.ba36bf010c6e73108fb4.js  5.19 MB       1  [emitted]  [big]  main
  b06871f281fee6b241d60582ae9369b9.ttf   166 kB          [emitted]
      manifest.c8c9fe6b5c67b40dd60c.js  1.62 kB       3  [emitted]         manifest
         0.279ec850a9242db04c85.js.map  1.36 MB       0  [emitted]
      main.ba36bf010c6e73108fb4.js.map  18.2 MB       1  [emitted]         main
    vendor.945719a65376e0552de5.js.map  5.69 MB       2  [emitted]         vendor
  manifest.c8c9fe6b5c67b40dd60c.js.map  8.24 kB       3  [emitted]         manifest
                            index.html  1.53 kB          [emitted]
[/sZe] ./~/@phosphor/commands/lib/index.js 33.3 kB {2} [built]
[2Kj9] ./~/@phosphor/widgets/lib/index.js 1.38 kB {2} [built]
[kzCB] ./~/path-posix/index.js 6.94 kB {2} [built]
[l9te] ./~/@phosphor/application/lib/index.js 18.1 kB {2} [built]
[lMhA] ./~/@phosphor/dragdrop/lib/index.js 33.7 kB {2} [built]
[nh00] ./~/@phosphor/disposable/lib/index.js 4.24 kB {2} [built]
[o73R] ./~/sanitize-html/index.js 11.2 kB {2} [built]
[q1RZ] ./~/@phosphor/datagrid/lib/index.js 793 bytes {2} [built]
[qzHn] ./~/@phosphor/coreutils/lib/index.js 721 bytes {2} [built]
[rplX] ./~/whatwg-fetch/fetch.js 13 kB {1} [built]
[ug+F] ./~/xterm/lib/xterm.js 52.7 kB {2} [built]
[wr2+] ./~/@phosphor/properties/lib/index.js 6.58 kB {2} [built]
[wuIn] ./~/comment-json/index.js 103 bytes {2} [built]
   [8] multi @phosphor/algorithm @phosphor/application @phosphor/commands @phosphor/coreutils @phosphor/datagrid @phosphor/disposable @phosphor/domutils @phosphor/dragdrop @phosphor/messaging @phosphor/properties @phosphor/signaling @phosphor/virtualdom @phosphor/widgets ajv ansi_up codemirror comment-json es6-promise marked moment path-posix react react-dom sanitize-html url-parse xterm 328 bytes {2} [built]
   [9] multi whatwg-fetch ./build/index.out.js 40 bytes {1} [built]
    + 2229 hidden modules
Child html-webpack-plugin for "index.html":
    [3IRH] (webpack)/buildin/module.js 517 bytes {0} [built]
    [DuR2] (webpack)/buildin/global.js 509 bytes {0} [built]
    [GTAU] ./~/html-loader!./templates/partial.html 420 bytes {0} [built]
    [M4fF] ./~/lodash/lodash.js 540 kB {0} [built]
    [vxCX] ./~/html-webpack-plugin/lib/loader.js!./templates/template.html 1.41 kB {0} [built]
✨  Done in 61.27s.
~~~

## vim

~~~bash
$ jupyter labextension install jupyterlab_vim
~~~

~~~bash 
> /Users/hide/.anyenv/envs/ndenv/shims/npm pack jupyterlab_vim
npm notice
npm notice 📦  jupyterlab_vim@0.9.0
npm notice === Tarball Contents ===
npm notice 1.3kB  package.json
npm notice 1.3kB  History.md
npm notice 1.1kB  LICENSE
npm notice 3.3kB  README.md
npm notice 229B   lib/index.d.ts
npm notice 20.4kB lib/index.js
npm notice 0      style/index.css
npm notice === Tarball Details ===
npm notice name:          jupyterlab_vim
npm notice version:       0.9.0
npm notice filename:      jupyterlab_vim-0.9.0.tgz
npm notice package size:  6.3 kB
npm notice unpacked size: 27.6 kB
npm notice shasum:        0faf1eddbfe018b591529e002fa73b161d021153
npm notice integrity:     sha512-uJbqfo48YqJXs[...]LTIvboLhlIGcg==
npm notice total files:   7
npm notice
jupyterlab_vim-0.9.0.tgz
> /Users/hide/.anyenv/envs/ndenv/shims/npm pack jupyterlab_vim@0.7.0
npm notice
npm notice 📦  jupyterlab_vim@0.7.0
npm notice === Tarball Contents ===
npm notice 1.3kB  package.json
npm notice 1.1kB  History.md
npm notice 1.1kB  LICENSE
npm notice 3.3kB  README.md
npm notice 229B   lib/index.d.ts
npm notice 20.4kB lib/index.js
npm notice 0      style/index.css
npm notice === Tarball Details ===
npm notice name:          jupyterlab_vim
npm notice version:       0.7.0
npm notice filename:      jupyterlab_vim-0.7.0.tgz
npm notice package size:  6.3 kB
npm notice unpacked size: 27.4 kB
npm notice shasum:        beae2839a9a8ef6e31f956fde9931af3763ba2ae
npm notice integrity:     sha512-6CMqMc+3dcF69[...]lwJbUK4i65CcQ==
npm notice total files:   7
npm notice
jupyterlab_vim-0.7.0.tgz
Incompatible extension:

"jupyterlab_vim@0.9.0" is not compatible with the current JupyterLab
Conflicting Dependencies:
JupyterLab              Extension        Package
>=0.16.3 <0.17.0        >=0.18.0 <0.19.0 @jupyterlab/application
>=0.16.3 <0.17.0        >=0.18.0 <0.19.0 @jupyterlab/notebook

Found compatible version: 0.7.0
> /Users/hide/.anyenv/envs/ndenv/shims/npm pack jupyterlab_vim@0.7.0
npm notice
npm notice 📦  jupyterlab_vim@0.7.0
npm notice === Tarball Contents ===
npm notice 1.3kB  package.json
npm notice 1.1kB  History.md
npm notice 1.1kB  LICENSE
npm notice 3.3kB  README.md
npm notice 229B   lib/index.d.ts
npm notice 20.4kB lib/index.js
npm notice 0      style/index.css
npm notice === Tarball Details ===
npm notice name:          jupyterlab_vim
npm notice version:       0.7.0
npm notice filename:      jupyterlab_vim-0.7.0.tgz
npm notice package size:  6.3 kB
npm notice unpacked size: 27.4 kB
npm notice shasum:        beae2839a9a8ef6e31f956fde9931af3763ba2ae
npm notice integrity:     sha512-6CMqMc+3dcF69[...]lwJbUK4i65CcQ==
npm notice total files:   7
npm notice
jupyterlab_vim-0.7.0.tgz
> node /Users/hide/.anyenv/envs/pyenv/versions/anaconda3-5.2.0/lib/python3.6/site-packages/jupyterlab/staging/yarn.js install
yarn install v1.5.1
info No lockfile found.
[1/4] 🔍  Resolving packages...
warning @jupyterlab/plotly-extension > plotly.js > mapbox-gl > @mapbox/gl-matrix@0.0.1: This
warning @jupyterlab/plotly-extension > plotly.js > ndarray-fill > cwise > static-module > through2 > xtend > object-keys@0.4.0:
warning css-loader > cssnano > autoprefixer > browserslist@1.7.7: Browserslist 2 could fail on reading Browserslist >3.0 config used in other tools.
warning css-loader > cssnano > postcss-merge-rules > browserslist@1.7.7: Browserslist 2 could fail on reading Browserslist >3.0 config used in other tools.
warning css-loader > cssnano > postcss-merge-rules > caniuse-api > browserslist@1.7.7: Browserslist 2 could fail on reading Browserslist >3.0 config used in other tools.
[2/4] 🚚  Fetching packages...
[3/4] 🔗  Linking dependencies...
warning "@jupyterlab/json-extension > react-json-tree@0.10.9" has incorrect peer dependency "react@^15.0.0".
warning "@jupyterlab/json-extension > react-json-tree@0.10.9" has incorrect peer dependency "react-dom@^15.0.0".
warning "@jupyterlab/vdom-extension > @nteract/transform-vdom@1.1.1" has incorrect peer dependency "react@^15.6.1".
[4/4] 📃  Building fresh packages...
success Saved lockfile.
✨  Done in 97.58s.
> node /Users/hide/.anyenv/envs/pyenv/versions/anaconda3-5.2.0/lib/python3.6/site-packages/jupyterlab/staging/yarn.js run build:prod
yarn run v1.5.1
$ webpack --config webpack.prod.config.js
Hash: 40b38a556f0f46775cd0
Version: webpack 2.7.0
Time: 75493ms
                                 Asset     Size  Chunks                    Chunk Names
        vendor.945719a65376e0552de5.js  1.57 MB       2  [emitted]  [big]  vendor
  912ec66d7572ff821749319396470bde.svg   444 kB          [emitted]  [big]
  674f50d287a8c48dc19ba404d20fe713.eot   166 kB          [emitted]
 fee66e712a8a08eef5805a46892932ad.woff    98 kB          [emitted]
af7ae505a9eed503f8b8e6982036873e.woff2  77.2 kB          [emitted]
             0.279ec850a9242db04c85.js   465 kB       0  [emitted]  [big]
          main.76accdb0bf2f4a87f06a.js   5.2 MB       1  [emitted]  [big]  main
  b06871f281fee6b241d60582ae9369b9.ttf   166 kB          [emitted]
      manifest.a8e4a26cdaf5ad776c2c.js  1.62 kB       3  [emitted]         manifest
         0.279ec850a9242db04c85.js.map  1.36 MB       0  [emitted]
      main.76accdb0bf2f4a87f06a.js.map  18.3 MB       1  [emitted]         main
    vendor.945719a65376e0552de5.js.map  5.69 MB       2  [emitted]         vendor
  manifest.a8e4a26cdaf5ad776c2c.js.map  8.24 kB       3  [emitted]         manifest
                            index.html  1.53 kB          [emitted]
[/sZe] ./~/@phosphor/commands/lib/index.js 33.3 kB {2} [built]
[2Kj9] ./~/@phosphor/widgets/lib/index.js 1.38 kB {2} [built]
[kzCB] ./~/path-posix/index.js 6.94 kB {2} [built]
[l9te] ./~/@phosphor/application/lib/index.js 18.1 kB {2} [built]
[lMhA] ./~/@phosphor/dragdrop/lib/index.js 33.7 kB {2} [built]
[nh00] ./~/@phosphor/disposable/lib/index.js 4.24 kB {2} [built]
[o73R] ./~/sanitize-html/index.js 11.2 kB {2} [built]
[q1RZ] ./~/@phosphor/datagrid/lib/index.js 793 bytes {2} [built]
[qzHn] ./~/@phosphor/coreutils/lib/index.js 721 bytes {2} [built]
[rplX] ./~/whatwg-fetch/fetch.js 13 kB {1} [built]
[ug+F] ./~/xterm/lib/xterm.js 52.7 kB {2} [built]
[wr2+] ./~/@phosphor/properties/lib/index.js 6.58 kB {2} [built]
[wuIn] ./~/comment-json/index.js 103 bytes {2} [built]
   [8] multi @phosphor/algorithm @phosphor/application @phosphor/commands @phosphor/coreutils @phosphor/datagrid @phosphor/disposable @phosphor/domutils @phosphor/dragdrop @phosphor/messaging @phosphor/properties @phosphor/signaling @phosphor/virtualdom @phosphor/widgets ajv ansi_up codemirror comment-json es6-promise marked moment path-posix react react-dom sanitize-html url-parse xterm 328 bytes {2} [built]
   [9] multi whatwg-fetch ./build/index.out.js 40 bytes {1} [built]
    + 2232 hidden modules
Child html-webpack-plugin for "index.html":
    [3IRH] (webpack)/buildin/module.js 517 bytes {0} [built]
    [DuR2] (webpack)/buildin/global.js 509 bytes {0} [built]
    [GTAU] ./~/html-loader!./templates/partial.html 420 bytes {0} [built]
    [M4fF] ./~/lodash/lodash.js 540 kB {0} [built]
    [vxCX] ./~/html-webpack-plugin/lib/loader.js!./templates/template.html 1.41 kB {0} [built]
✨  Done in 77.12s.
~~~