~~~py
from tempfile import TemporaryFile
t = TemporaryFile()
data = 'A simple string of text.'
~~~

~~~py
>>> t.write(data)
>>> # Makes sure the marker is at the start of the file
>>> t.seek(0)
>>> print(t.read())
A simple string of text.
~~~

~~~py
with TemporaryFile() as tempf:
    tempf.write((data + '\n') * 3)
    tempf.seek(0)
    print(tempf.read())
~~~    
