## メッセージクラス

~~~py
In [5]: from django.core.mail import EmailMessage
In [6]: email = EmailMessage('Hello', 'World', to=['user@gmail.com'])
In [7]: type(email)
Out[7]: django.core.mail.message.EmailMessage
In [9]: msg = email.message()
In [10]: type(msg)
Out[10]: instance
In [12]: print msg.as_bytes(linesep='\r\n')
MIME-Version: 1.0
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 7bit
Subject: Hello
From: webmaster@localhost
To: user@gmail.com
Date: Thu, 20 Oct 2016 03:27:24 -0000
Message-ID: <20161020032724.15784.44944@10.0.2.15>

World
~~~
