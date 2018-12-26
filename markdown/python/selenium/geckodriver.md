# geckodriver

## Ubuntu

~~~bash
$ sudo apt-get install firefox
~~~

パスを通しておく:

~~~bash
$ cd /usr/local/bin
$ curl -L https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz | sudo tar zxv
~~~

~~~bash
$ geckodriver --version
geckodriver 0.23.0 ( 2018-10-04)

The source code of this program is available from
testing/geckodriver in https://hg.mozilla.org/mozilla-central.

This program is subject to the terms of the Mozilla Public License 2.0.
You can obtain a copy of the license at https://mozilla.org/MPL/2.0/.
~~~

~~~py
from selenium import webdriver

options = webdriver.FirefoxOptions()
options.add_argument('-headless')

driver = webdriver.Firefox(options=options)
driver.get('https://www.google.co.jp/')

print(driver.title)
~~~