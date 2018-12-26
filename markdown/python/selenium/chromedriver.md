# Chrome Driver

- [chromedriver-binary](https://pypi.org/project/chromedriver-binary/)

~~~bash
$ pip install chromedriver-binary

Collecting chromedriver-binary
  Downloading https://files.pythonhosted.org/packages/fb/69/bee1761411365dc26d82dcad2b05b900917b234c0682453f4afa623fc0c8/chromedriver-binary-2.45.0.tar.gz
Installing collected packages: chromedriver-binary
  Running setup.py install for chromedriver-binary ... done
Successfully installed chromedriver-binary-2.45.0
~~~

~~~py
from selenium import webdriver
import chromedriver_binary  # PATHが通る

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get("http://www.python.org")

assert "Python" in driver.title
print(driver.title)
~~~