# VSCode

## Vagrant

~~~bash
$ pip install django-ptvsd-debug
.
~~~

settings.py:

~~~py
INSTALLED_APPS = ['django_ptvsd'] + INSTALLED_APPS
PTVSD_REMOTE_PORT = 3000
~~~

~~~bash
$ python manage.py runserver 0.0.0.0:9000 --ptvsd

PTVSD: Enabled Attach (0.0.0.0:3000)
Watching for file changes with StatReloader
Performing system checks...
~~~

## macOS

- anyenv
.bash_profile:

~~~bash
...
export PATH="$HOME/.anyenv/bin:$PATH"
eval "$(anyenv init -)"
~~~

~~~bash
$ echo $(pyenv prefix)

/Users/hide/.anyenv/envs/pyenv/versions/anaconda3-2019.03
~~~

VSCode: `Code` >  `基本設定` >  `設定`:

~~~json
{
    "python.pythonPath": "/Users/hide/.anyenv/envs/pyenv/versions/anaconda3-2019.03/bin/python"
}
~~~

## プロジェクト

~~~bash
$ tree .vscode/
.vscode/
└── launch.json
~~~

launch.json:

~~~json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "attach",
            "port": 3000,
            "host": "vagrant.local",
            "pathMappings": [
                {
                    "localRoot": "${workspaceFolder}/reform/web",
                    "remoteRoot": "/home/vagrant/projects/sites/reform/web"
                }
            ]
        }
    ]
}
~~~

~~~bash
$ lsof -i:3000
COMMAND     PID USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
Code\x20H 30345 hide   26u  IPv4 0xbcf9f8bc05689799      0t0  TCP 192.168.56.1:60745->taberu.local:hbci (ESTABLISHED)
~~~

## 記事

- [[macOS]   PyenvでPython使う (VSCode)](https://qiita.com/andromeda/items/2e5a89a89cecb11b29f2)
- [Docker上で動くgunicorn + DjangoアプリケーションをVS Codeからリモートデバッグする](https://qiita.com/hashiyaman/items/ab3b538503afa0516832)
- [Python Remote Debug](https://qiita.com/kenmasu/items/c46804a30f83bbfc18c8)
- [django-ptvsd-debug · PyPI](https://pypi.org/project/django-ptvsd-debug/)
