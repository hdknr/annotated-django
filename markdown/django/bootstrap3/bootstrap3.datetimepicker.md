## Bootstrap

- http://eonasdan.github.io/bootstrap-datetimepicker/

### settings.py

~~~py
BOWER_INSTALLED_APPS = [                                                            
    'jquery',                                                                       
    'moment',               # http://momentjs.com/                                  
    'eonasdan-bootstrap-datetimepicker',    # https://eonasdan.github.io/bootstrap-datetimepicker/Installing/   # NOQA
]                                                                                   
~~~

### script


~~~html
<script src="{% static 'jquery/dist/jquery.min.js' %}"></script>
<script src="{% static 'moment/moment.js' %}"></script>
<script src="{% static 'moment/locale/ja.js' %}"></script>
<script src="{% static 'eonasdan-bootstrap-datetimepicker/src/js/bootstrap-datetimepicker.js' %}"></script>
~~~

### page

- [moment format](http://momentjs.com/docs/#/displaying/format/)

~~~html
<script type="text/javascript">
    $(function () {
        $('#id_available_at').datetimepicker({ locale: 'ja', format: 'YYYY-MM-DD hh:mm:ss' });
    });
</script>
~~~

## jquery-ui

- https://github.com/xdan/datetimepicker    

### settings.py

~~~py
BOWER_INSTALLED_APPS = [                                                         
    'jquery',                                                                    
    'jquery-ui',                                                                 
    'datetimepicker',       # https://github.com/xdan/datetimepicker             
]                           
~~~

### css

~~~html
<link href="{% static 'datetimepicker/jquery.datetimepicker.css' %}" rel="stylesheet">
~~~

### scripts

~~~html
<script src="{% static 'datetimepicker/build/jquery.datetimepicker.full.js' %}"></script>
~~~

### page

~~~html
<script type="text/javascript">
    $(function () {
        $.datetimepicker.setLocale('ja');
        $("#id_expire_at").datetimepicker({
          lang: 'ja', format: 'Y-m-d H:i', defaultTime: '10:00', timepickerScrollbar: false
        });
    });
</script>
~~~
