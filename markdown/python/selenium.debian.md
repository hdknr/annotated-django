~~~bash
$ sudo apt-get install firefox-esr
~~~

~~~bash
$ sudo apt-get install libdbus-glib-1-2
$ sudo apt-get install libgtk2.0-0
$ sudo apt-get install libasound2
~~~

~~~bash
$ pip install pyvirtualdisplay
Collecting pyvirtualdisplay
  Downloading PyVirtualDisplay-0.2.tar.gz
Collecting EasyProcess (from pyvirtualdisplay)
  Downloading EasyProcess-0.2.2.tar.gz
Building wheels for collected packages: pyvirtualdisplay, EasyProcess
  Running setup.py bdist_wheel for pyvirtualdisplay ... done
  Stored in directory: /home/vagrant/.cache/pip/wheels/31/c4/d8/65185e1c3c06e41c003ee5c99941d30ed86119f7e6c9438b50
  Running setup.py bdist_wheel for EasyProcess ... done
  Stored in directory: /home/vagrant/.cache/pip/wheels/6f/f1/de/dd7f2f17296e6280646245dc107fb8df835384cd1591042daf
Successfully built pyvirtualdisplay EasyProcess
Installing collected packages: EasyProcess, pyvirtualdisplay
Successfully installed EasyProcess-0.2.2 pyvirtualdisplay-0.2
~~~

## テスト

~~~py
from pyvirtualdisplay import Display                                                
from selenium import webdriver                                                      
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary                 

display = Display(visible=0, size=(800, 600))                                       
display.start()                                                                     

ffbin = FirefoxBinary(                                                              
    firefox_path='/usr/lib/firefox-esr/firefox-bin',                                
    log_file=open("/tmp/ff.log", "w"))                                              
browser = webdriver.Firefox(firefox_binary=ffbin)                                   
browser.get('http://www.apple.com/')                                                
print browser.page_source                                                           
display.stop()                                                                      
~~~

##  Message: The browser appears to have exited before we could connect.

~~~
XPCOMGlueLoad error for file /opt/firefox/libmozgtk.so:
libgtk-3.so.0: cannot open shared object file: No such file or directory
Couldn't load XPCOM.
~~~

~~~bash
$ sudo apt-get install libgtk-3-0
~~~
