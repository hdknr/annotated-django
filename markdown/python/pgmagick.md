- [pgmagick](https://pypi.python.org/pypi/pgmagick/)
- https://github.com/hhatto/pgmagick
- https://pgmagick.readthedocs.io/en/latest/
- [Magick++ API for GraphicsMagick](http://www.graphicsmagick.org/Magick++/)

## Debian

~~~bash
$ sudo apt-get update
$ sudo apt-get install libmagick++-dev libgraphicsmagick++1-dev libboost-python-dev
~~~

~~~bash
$ sudo apt-get install fonts-ipafont
~~~

## Sample

- density : DPI

~~~py
In [1]: from pgmagick.api import Image
In [2]: i = Image('../../web/media/public/events_event_attachment/test-pdf.pdf')
In [3]: i.img.density = "3600x3600"
In [4]: i.write('/tmp/hoge.png')
~~~

## Geometry  (DPI)

~~~py
In [2]: from pgmagick import Geometry
In [3]: Geometry(3200, 3200)
Out[3]: <pgmagick.Geometry at 0x7f40d8a0b578>
In [4]: i = Image('tact-2015.pdf[1]')
In [5]: i.img.density(Geometry(12000, 1200))
In [6]: i.write('tact-2015.1.png')
~~~

## size

- 元画像から切り取られる

~~~py
In [16]: i.img.size(Geometry(400, 400))
In [17]: i.write('tact-2015.400x400.png')   
~~~

## undefined symbol: PyUnicodeUCS4_FromEncodedObject

~~~bash
In [1]: from pgmagick.api import Image
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)
<ipython-input-1-58454ea56503> in <module>()
----> 1 from pgmagick.api import Image

/home/vagrant/.anyenv/envs/pyenv/versions/sandbox/lib/python2.7/site-packages/pgmagick/__init__.py in <module>()
----> 1 from pgmagick import _pgmagick
      2
      3
      4 def __init():
      5     _pgmagick.InitializeMagick("./")

ImportError: /usr/lib/x86_64-linux-gnu/libboost_python-py27.so.1.55.0: undefined symbol: PyUnicodeUCS4_FromEncodedObject
~~~

- virtualenv のコンパイルオプションで UCS4 を有効にする

~~~bash
$ PYTHON_CONFIGURE_OPTS="--enable-unicode=ucs4" pyenv install 2.7.11
pyenv: /home/vagrant/.anyenv/envs/pyenv/versions/2.7.11 already exists
continue with installation? (y/N) y
Installing Python-2.7.11...
~~~

- virtualenv を再度更新

~~~bash
$ pyenv virtualenv -f 2.7.11 sandbox
~~~

## fpdf

- これはHTML+CSSからPDFを作るツールですので用途は違います
- http://pyfpdf.readthedocs.io/en/latest/

~~~bash
$ pip install fpdf
~~~
