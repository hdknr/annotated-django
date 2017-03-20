## gunicorn.access.log が記録されない

~~~py
disable_existing_loggers=False
~~~

## gunicorn.log ローテーション

nginx:

~~~py
/home/system/projects/shipping/web/logs/*.log {
    daily
    missingok
    rotate 104
    compress
    delaycompress
    notifempty
    su system users
    create 0640 system users
    sharedscripts
    postrotate
        kill -USR1 $(cat /home/system/projects/shopping/web/logs/gunicorn.pid)
    endscript
}
~~~
