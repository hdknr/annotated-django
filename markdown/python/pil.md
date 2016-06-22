##  The _imagingft C module is not installed

- [Python: The _imagingft C module is not installed](http://stackoverflow.com/questions/4011705/python-the-imagingft-c-module-is-not-installed)

Debian:

~~~
$ sudo aptitude install libfreetype6-dev
~~~

OSX:

~~~
$ brew install freetype
~~~


再インストール

~~~
$ pip uninstall pillow
$ pip install --no-cache-dir pillow
~~~

## 画像マージ

~~~python
a_jpg = im.open("{image_a}") # size(100,100)
b_jpg = im.open("{image_b}") # size(100,100)

canvas = im.new("RGB",(xxx,xxx),(255,255,255))

canvas.paste(a_jpg,(0,0))
canvas.paste(a_jpg,(0,100))
canvas.save('c.jpg', 'JPEG', quality=100, optimize=True)
~~~
