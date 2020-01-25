# marshmallow

- https://github.com/marshmallow-code/marshmallow

## marshmallow-dataclass

- https://github.com/lovasoa/marshmallow_dataclass
- https://github.com/ilevkivskyi/typing_inspect
- http://www.mypy-lang.org/

~~~bash
$ pip install marshmallow_dataclass -U

Collecting marshmallow_dataclass
  Using cached https://files.pythonhosted.org/packages/12/ca/f2dc27685df46a13e0a677df927743d201cda4f00e26d25d3405f014df0b/marshmallow_dataclass-6.0.0.tar.gz
Collecting marshmallow<4.0,>=3.0.0 (from marshmallow_dataclass)
  Using cached https://files.pythonhosted.org/packages/78/8c/aa99cd72e69ce14c754a4df752a57faffbd698b14a6fda598a3950273e99/marshmallow-3.2.1-py2.py3-none-any.whl
Collecting typing-inspect (from marshmallow_dataclass)
  Using cached https://files.pythonhosted.org/packages/ea/48/46ba0aff9c6ea0f6db6a0a62559298a9fe448316d06b797200595d77d0c0/typing_inspect-0.4.0-py3-none-any.whl
Requirement already satisfied, skipping upgrade: dataclasses in /Users/hide/.anyenv/envs/pyenv/versions/anaconda3-5.2.0/lib/python3.6/site-packages (from marshmallow_dataclass) (0.6)
Collecting mypy-extensions>=0.3.0 (from typing-inspect->marshmallow_dataclass)
Building wheels for collected packages: marshmallow-dataclass
  Building wheel for marshmallow-dataclass (setup.py) ... done
  Stored in directory: /Users/hide/Library/Caches/pip/wheels/4c/b6/78/377ee0ba060cefa1693eea60673451a900be60c0f05b45807c
Successfully built marshmallow-dataclass
Installing collected packages: marshmallow, mypy-extensions, typing-inspect, marshmallow-dataclass
Successfully installed marshmallow-3.2.1 marshmallow-dataclass-6.0.0 mypy-extensions-0.4.2 typing-inspect-0.4.0
~~~
