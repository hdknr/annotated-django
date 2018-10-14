# サブプロセス管理

- [17.5. subprocess — サブプロセス管理 — Python 3.6.5 ドキュメント](https://docs.python.jp/3.6/library/subprocess.html)

## at コマンド実行

`at` コマンドに `stdin` でコマンドを指定する:

~~~py
def run_at(command, dt):
    '''execute command at specifed datetime'''
    sched_cmd = ['/usr/bin/at', dt.strftime('%H:%M %m/%d/%Y')]
    subprocess.Popen(sched_cmd, stdin=subprocess.PIPE).communicate(command.encode('utf8'))
~~~

## 記事

- [Python の subprocess で出力を受け取るときは communicate() を使おう - Qiita](https://qiita.com/mokemokechicken/items/a84b0aa96b94d1931f08)
- [subprocessの使い方(Python3.6) - Qiita](https://qiita.com/caprest/items/0245a16825789b0263ad)