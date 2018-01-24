pyexcel:

- https://github.com/pyexcel/pyexcel
- https://github.com/pyexcel/pyexcel-xlsx
- RTD: https://pyexcel.readthedocs.io/en/latest/

## Install

~~~bash
$ pip install pyexcel-xlsx
Collecting pyexcel-xlsx
  Downloading pyexcel_xlsx-0.5.5-py2.py3-none-any.whl
Collecting pyexcel-io>=0.5.3 (from pyexcel-xlsx)
  Downloading pyexcel_io-0.5.6-py2.py3-none-any.whl (42kB)
    100% |████████████████████████████████| 51kB 1.1MB/s
Collecting openpyxl>=2.4.4 (from pyexcel-xlsx)
  Downloading openpyxl-2.4.10.tar.gz (158kB)
    100% |████████████████████████████████| 163kB 1.1MB/s
Collecting lml==0.0.1 (from pyexcel-io>=0.5.3->pyexcel-xlsx)
  Downloading lml-0.0.1-py2.py3-none-any.whl
Requirement already satisfied: jdcal in /Users/hide/.anyenv/envs/pyenv/versions/anaconda3-4.3.1/lib/python3.6/site-packages (from openpyxl>=2.4.4->pyexcel-xlsx)
Requirement already satisfied: et_xmlfile in /Users/hide/.anyenv/envs/pyenv/versions/anaconda3-4.3.1/lib/python3.6/site-packages (from openpyxl>=2.4.4->pyexcel-xlsx)
Building wheels for collected packages: openpyxl
  Running setup.py bdist_wheel for openpyxl ... done
  Stored in directory: /Users/hide/Library/Caches/pip/wheels/65/83/ad/9b2481b895e3fe9b55606eee4b35ef3cd14bd8c018dc2a9c53
Successfully built openpyxl
Installing collected packages: lml, pyexcel-io, openpyxl, pyexcel-xlsx
  Found existing installation: openpyxl 2.4.1
    Uninstalling openpyxl-2.4.1:
      Successfully uninstalled openpyxl-2.4.1
Successfully installed lml-0.0.1 openpyxl-2.4.10 pyexcel-io-0.5.6 pyexcel-xlsx-0.5.5
~~~

[jupyter](https://github.com/hdknr/annotated-django/issues/39):

~~~bash
$ jupyter notebook
~~~



```python
import pyexcel_xlsx as P
wb = P.get_data('/Users/hide/Desktop/YamatoShipping.xlsx')
wb.keys()
```

    odict_keys(['基本配送料金'])

```python
import json
print(json.dumps(wb, indent=2, ensure_ascii=False))
```

    {
      "基本配送料金": [
        [
          "",
          "常温",
          "冷蔵",
          "冷凍",
          "全温度"
        ],
        [
          "北海道",
          1000,
          1200,
          1200,
          1000
        ],
        ....
        [
          "沖縄県",
          1046,
          1246,
          1246,
          1046
        ]
      ]
    }
