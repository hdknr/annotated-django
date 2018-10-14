# Excel ライブラリ

- [openpyxl](http://openpyxl.readthedocs.org/en/default/)
- [XlsxWriter](https://xlsxwriter.readthedocs.org/)
- [xlwt](https://pypi.python.org/pypi/xlwt)
- [xlrd](https://pypi.python.org/pypi/xlrd) (http://www.python-excel.org/)
- [xlwings](http://xlwings.org/)
- [xlutils](http://pythonhosted.org/xlutils/)
- [python-xlsx](https://github.com/python-openxml/python-xlsx)
- [pandas](https://pandas.pydata.org/)

## 記事

- [PythonでExcelファイルを扱うライブラリの比較 | note.nkmk.me](https://note.nkmk.me/python-excel-library/)

## XlsxWriter

~~~
XlsxWriter can only create new files. It cannot read or modify existing files.
~~~

- [Working with Python Pandas and XlsxWriter](http://xlsxwriter.readthedocs.org/working_with_pandas.html)

## Others...

- [Alternative modules for handling Excel files](https://xlsxwriter.readthedocs.org/alternatives.html#alternatives)
- [XLRD vs OPENPYXL, Round II](http://poquitopicante.blogspot.jp/2013/06/xlrd-vs-openpyxl-round-ii.html)
- [A Python script that uses the xlrd and openpyxl frameworks to read user defined cells from a selected Excel spreadsheet and append them to a seperate master workbook.](https://gist.github.com/duketon/9487942)

## Wordは ...

- [python-openxml](https://github.com/python-openxml)
- [python-docx](https://python-docx.readthedocs.org/en/latest/) | [github](https://github.com/python-openxml/python-docx)



## openpyxl

### rows

- 'openpyxl.cell.cell.Cell' オブジェクトの tuple です

### Cell

- [openpyxl.cell.cell.Cell](http://openpyxl.readthedocs.io/en/default/api/openpyxl.cell.cell.html)

- 行と列: `row` (int), `column` (str)


## pandas 

~~~bash 
$ pip install pandas xlrd
~~~

### DataFrame

- [DataFrame](https://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe)
- [Pandasのデータを格納するオブジェクトDataFrameを理解する - DeepAge](https://deepage.net/features/pandas-dataframe.html)


### 例

~~~py
from math import isnan, nan
import pandas as pd


def _value(value):
    if isinstance(value, float) and isnan(value):
        return None
    return value


def open_excel(path):
    return pd.ExcelFile(path, encoding='utf8')


def allsheets(path, **parser):   
    file = open_excel(path)
    for i, name in enumerate(file.sheet_names):
       yield i, name, file.parse(name, **parser)


def impor_product_sheet(sheet):
    from .modles import Product
    for index, row in sheet.iterrows():
        params = list(dict(
            (key, _value(value))
            for key, value in  row.to_dict().items()
        ).items())
        keys = dict(params[:2])
        values = dict(params[2:])
        if Product.objects.filter(**keys).update(**values) < 1:
            values.update(keys)
            Product.objects.create(**values)

def import_product_file(path):

    for i, name, sheet in sheets.allsheets(path):
        import_product_sheet(sheet)

~~~

### 記事

- [pandasでExcelファイル（xlsx, xls）の読み込み（read_excel） | note.nkmk.me](https://note.nkmk.me/python-pandas-read-excel/)
- [pythonでexcelファイル処理まとめ - Qiita](https://qiita.com/hasepy/items/06d5d2e2b6495752442c)
