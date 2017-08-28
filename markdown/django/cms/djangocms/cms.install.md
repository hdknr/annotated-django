- http://docs.django-cms.org/en/release-3.4.x/introduction/install.html



~~~bash
$ pip install djangocms-installer

Collecting djangocms-installer
  Downloading djangocms_installer-0.9.7-py2.py3-none-any.whl (58kB)
    100% |████████████████████████████████| 61kB 1.7MB/s
Collecting dj-database-url>=0.4 (from djangocms-installer)
  Downloading dj_database_url-0.4.2-py2.py3-none-any.whl
Requirement already satisfied: pip in /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/lib/python3.6/site-packages (from djangocms-installer)
Collecting argparse (from djangocms-installer)
  Downloading argparse-1.4.0-py2.py3-none-any.whl
Collecting tzlocal (from djangocms-installer)
  Downloading tzlocal-1.4.tar.gz
Requirement already satisfied: six in /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/lib/python3.6/site-packages (from djangocms-installer)
Requirement already satisfied: pytz in /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/lib/python3.6/site-packages (from tzlocal->djangocms-installer)
Installing collected packages: dj-database-url, argparse, tzlocal, djangocms-installer
  Running setup.py install for tzlocal ... done
Successfully installed argparse-1.4.0 dj-database-url-0.4.2 djangocms-installer-0.9.7 tzlocal-1.4
~~~


~~~bash
$ djangocms mysite

Creating the project
Please wait while I install dependencies
Dependencies installed
Creating the project
Operations to perform:
  Synchronize unmigrated apps: sekizai, cmsplugin_filer_utils, staticfiles, treebeard, messages, mysite, djangocms_admin_style, sitemaps
  Apply all migrations: cmsplugin_filer_folder, djangocms_text_ckeditor, auth, sites, djangocms_link, djangocms_snippet, cmsplugin_filer_image, admin, djangocms_style, sessions, menus, djangocms_googlemap, cms, contenttypes, easy_thumbnails, djangocms_video, filer, cmsplugin_filer_file, djangocms_column
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying sites.0001_initial... OK
  Applying cms.0001_initial... OK
  Applying cms.0002_auto_20140816_1918... OK
  Applying cms.0003_auto_20140926_2347... OK
  Applying cms.0004_auto_20140924_1038... OK
  Applying cms.0005_auto_20140924_1039... OK
  Applying cms.0006_auto_20140924_1110... OK
  Applying cms.0007_auto_20141028_1559... OK
  Applying cms.0008_auto_20150208_2149... OK
  Applying cms.0008_auto_20150121_0059... OK
  Applying cms.0009_merge... OK
  Applying cms.0010_migrate_use_structure... OK
  Applying cms.0011_auto_20150419_1006... OK
  Applying cms.0012_auto_20150607_2207... OK
  Applying cms.0013_urlconfrevision... OK
  Applying cms.0014_auto_20160404_1908... OK
  Applying cms.0015_auto_20160421_0000... OK
  Applying cms.0016_auto_20160608_1535... OK
  Applying filer.0001_initial... OK
  Applying cmsplugin_filer_file.0001_initial... OK
  Applying cmsplugin_filer_file.0002_auto_20160112_1617... OK
  Applying cmsplugin_filer_file.0003_filerfile_link_attributes... OK
  Applying cmsplugin_filer_file.0004_auto_20160705_1334... OK
  Applying cmsplugin_filer_file.0005_auto_20160713_1853... OK
  Applying cmsplugin_filer_folder.0001_initial... OK
  Applying cmsplugin_filer_folder.0002_auto_20160113_1318... OK
  Applying cmsplugin_filer_folder.0003_auto_20160713_1853... OK
  Applying filer.0002_auto_20150606_2003... OK
  Applying filer.0003_thumbnailoption... OK
  Applying cmsplugin_filer_image.0001_initial... OK
  Applying cmsplugin_filer_image.0002_auto_20160108_1708... OK
  Applying cmsplugin_filer_image.0003_mv_thumbnail_option_to_filer_20160119_1720... OK
  Applying cmsplugin_filer_image.0004_auto_20160120_0950... OK
  Applying cmsplugin_filer_image.0005_auto_20160224_1457... OK
  Applying cmsplugin_filer_image.0006_auto_20160427_1438... OK
  Applying cmsplugin_filer_image.0007_filerimage_link_attributes... OK
  Applying cmsplugin_filer_image.0008_auto_20160705_1334... OK
  Applying cmsplugin_filer_image.0009_auto_20160713_1853... OK
  Applying djangocms_column.0001_initial... OK
  Applying djangocms_column.0002_auto_20160915_0818... OK
  Applying filer.0004_auto_20160328_1434... OK
  Applying filer.0005_auto_20160623_1425... OK
  Applying filer.0006_auto_20160623_1627... OK
  Applying filer.0007_auto_20161016_1055... OK
  Applying djangocms_googlemap.0001_initial... OK
  Applying djangocms_googlemap.0002_auto_20160622_1031... OK
  Applying djangocms_googlemap.0003_auto_20160825_1829... OK
  Applying djangocms_googlemap.0004_adapted_fields... OK
  Applying djangocms_googlemap.0005_create_nested_plugins... OK
  Applying djangocms_googlemap.0006_remove_fields... OK
  Applying djangocms_googlemap.0007_reset_null_values... OK
  Applying djangocms_googlemap.0008_removed_null_fields... OK
  Applying djangocms_googlemap.0009_googlemapmarker_icon... OK
  Applying djangocms_link.0001_initial... OK
  Applying djangocms_link.0002_auto_20140929_1705... OK
  Applying djangocms_link.0003_auto_20150212_1310... OK
  Applying djangocms_link.0004_auto_20150708_1133... OK
  Applying djangocms_link.0005_auto_20151003_1710... OK
  Applying djangocms_link.0006_remove_related_name_for_cmsplugin_ptr... OK
  Applying djangocms_link.0007_set_related_name_for_cmsplugin_ptr... OK
  Applying djangocms_link.0008_link_attributes... OK
  Applying djangocms_link.0009_auto_20160705_1344... OK
  Applying djangocms_link.0010_adapted_fields... OK
  Applying djangocms_link.0011_fixed_null_values... OK
  Applying djangocms_link.0012_removed_null... OK
  Applying djangocms_link.0013_fix_hostname... OK
  Applying djangocms_snippet.0001_initial... OK
  Applying djangocms_snippet.0002_snippet_slug... OK
  Applying djangocms_snippet.0003_auto_data_fill_slug... OK
  Applying djangocms_snippet.0004_auto_alter_slug_unique... OK
  Applying djangocms_snippet.0005_set_related_name_for_cmsplugin_ptr... OK
  Applying djangocms_snippet.0006_auto_20160831_0729... OK
  Applying djangocms_snippet.0007_auto_alter_template_helptext... OK
  Applying djangocms_style.0001_initial... OK
  Applying djangocms_style.0002_set_related_name_for_cmsplugin_ptr... OK
  Applying djangocms_style.0003_adapted_fields... OK
  Applying djangocms_style.0004_use_positive_small_integer_field... OK
  Applying djangocms_style.0005_reset_null_values... OK
  Applying djangocms_style.0006_removed_null_fields... OK
  Applying djangocms_style.0007_style_template... OK
  Applying djangocms_text_ckeditor.0001_initial... OK
  Applying djangocms_text_ckeditor.0002_remove_related_name_for_cmsplugin_ptr... OK
  Applying djangocms_text_ckeditor.0003_set_related_name_for_cmsplugin_ptr... OK
  Applying djangocms_text_ckeditor.0004_auto_20160706_1339... OK
  Applying djangocms_video.0001_initial... OK
  Applying djangocms_video.0002_set_related_name_for_cmsplugin_ptr... OK
  Applying djangocms_video.0003_field_adaptions... OK
  Applying djangocms_video.0004_move_to_attributes... OK
  Applying djangocms_video.0005_migrate_to_filer... OK
  Applying djangocms_video.0006_field_adaptions... OK
  Applying djangocms_video.0007_create_nested_plugin... OK
  Applying djangocms_video.0008_reset_null_values... OK
  Applying djangocms_video.0009_removed_null_values... OK
  Applying easy_thumbnails.0001_initial... OK
  Applying easy_thumbnails.0002_thumbnaildimensions... OK
  Applying menus.0001_initial... OK
  Applying sessions.0001_initial... OK
Creating admin user
All done!
Get into "/vagrant/projects/hdknr/mysite" directory and type "python manage.py runserver" to start your project

~~~

~~~bash
$ tree mysite/
mysite/
├── manage.py
├── media
├── mysite
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   └── settings.cpython-36.pyc
│   ├── settings.py
│   ├── static
│   ├── templates
│   │   ├── base.html
│   │   ├── fullwidth.html
│   │   ├── sidebar_left.html
│   │   └── sidebar_right.html
│   ├── urls.py
│   └── wsgi.py
├── project.db
├── requirements.txt
└── static

6 directories, 13 files
~~~


~~~bash
$ cd mysite
$ python manage.py createsuperuser

Username (leave blank to use 'vagrant'):
Email address: vagrant@ubuntu.local
Password:
Password (again):
Superuser created successfully.
~~~


## Bootstrap

~~~bash
$ djangocms mysite2 --bootstrap yes
~~~
