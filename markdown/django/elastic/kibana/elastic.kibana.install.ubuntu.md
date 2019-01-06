# Kibana: Ubuntu

## Install on Ubuntu 17.10

- [Install Kibana with Debian Package](https://www.elastic.co/guide/en/kibana/current/deb.html)

~~~bash
$ wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

$ sudo apt-get install apt-transport-https

$ echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list
deb https://artifacts.elastic.co/packages/6.x/apt stable main

$ sudo apt-get update && sudo apt-get install kibana

$ dpkg -L kibana | grep "^/etc"
/etc
/etc/kibana
/etc/kibana/kibana.yml
/etc/default
/etc/default/kibana
/etc/systemd
/etc/systemd/system
/etc/systemd/system/kibana.service
/etc/init.d
/etc/init.d/kibana

$ sudo /etc/init.d/kibana start
kibana started

$ ps ax | grep kibana
 3458 pts/3    Rl     0:03 /usr/share/kibana/bin/../node/bin/node --no-warnings /usr/share/kibana/bin/../src/cli -c /etc/kibana/kibana.yml
 3478 pts/3    S+     0:00 grep --color=auto kibana

$ sudo lsof -u kibana
COMMAND  PID   USER   FD      TYPE DEVICE SIZE/OFF    NODE NAME
node    3458 kibana  cwd       DIR    8,1     4096       2 /
node    3458 kibana  rtd       DIR    8,1     4096       2 /
node    3458 kibana  txt       REG    8,1 30559647 2229925 /usr/share/kibana/node/bin/node
node    3458 kibana  mem       REG    8,1    47608 2246948 /lib/x86_64-linux-gnu/libnss_files-2.26.so
node    3458 kibana  mem       REG    8,1  1960656 2246938 /lib/x86_64-linux-gnu/libc-2.26.so
node    3458 kibana  mem       REG    8,1   144776 2246953 /lib/x86_64-linux-gnu/libpthread-2.26.so
node    3458 kibana  mem       REG    8,1    92520 2237701 /lib/x86_64-linux-gnu/libgcc_s.so.1
node    3458 kibana  mem       REG    8,1  1404912 2246942 /lib/x86_64-linux-gnu/libm-2.26.so
node    3458 kibana  mem       REG    8,1  1586608 1974355 /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.24
node    3458 kibana  mem       REG    8,1    31744 2246955 /lib/x86_64-linux-gnu/librt-2.26.so
node    3458 kibana  mem       REG    8,1    14632 2246941 /lib/x86_64-linux-gnu/libdl-2.26.so
node    3458 kibana  mem       REG    8,1   170960 2228722 /lib/x86_64-linux-gnu/ld-2.26.so
node    3458 kibana    0r      CHR    1,3      0t0       6 /dev/null
node    3458 kibana    1w      REG    8,1     1632  280045 /var/log/kibana/kibana.stdout
node    3458 kibana    2w      REG    8,1        0  280046 /var/log/kibana/kibana.stderr
node    3458 kibana    3r     FIFO   0,12      0t0   27743 pipe
node    3458 kibana    4w     FIFO   0,12      0t0   27743 pipe
node    3458 kibana    5u  a_inode   0,13        0    9012 [eventpoll]
node    3458 kibana    6r     FIFO   0,12      0t0   27744 pipe
node    3458 kibana    7w     FIFO   0,12      0t0   27744 pipe
node    3458 kibana    8u  a_inode   0,13        0    9012 [eventfd]
node    3458 kibana    9r      CHR    1,3      0t0       6 /dev/null
node    3458 kibana   10u     IPv4  27756      0t0     TCP localhost:5601 (LISTEN)
node    3458 kibana   11u     IPv4  27757      0t0     TCP localhost:35720->localhost:9200 (ESTABLISHED)


$ sudo lsof -i:5601
COMMAND  PID   USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
node    3458 kibana   10u  IPv4  27756      0t0  TCP localhost:5601 (LISTEN)

$ sudo vim /etc/kibana/kibana.yml
$ grep 0.0.0.0 /etc/kibana/kibana.yml
server.host: "0.0.0.0"

$ sudo /etc/init.d/kibana restart
kibana stopped.
kibana started


$ sudo lsof -i:5601
COMMAND  PID   USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
node    3553 kibana   11u  IPv4  29817      0t0  TCP *:5601 (LISTEN)
~~~
