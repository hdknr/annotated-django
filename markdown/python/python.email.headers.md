## From

- [Python email module: form header “From” with some unicode name + email](http://stackoverflow.com/questions/10551933/python-email-module-form-header-from-with-some-unicode-name-email)

~~~py
from email.MIMEMultipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr

author = formataddr((str(Header(u'Alał', 'utf-8')), "somemail@somedomain.com"))
msg = MIMEMultipart('alternative')
msg['From'] = author
print msg
~~~

~~~py
>>> Header(u'鈴木一朗', 'utf8')
<email.header.Header instance at 0x7fc46029a170>
>>> h = _
>>> print h
=?utf-8?b?6Yi05pyo5LiA5pyX?=

>>> formataddr((str(h), 'foo@bar.com'))
'=?utf-8?b?6Yi05pyo5LiA5pyX?= <foo@bar.com>'
~~~
