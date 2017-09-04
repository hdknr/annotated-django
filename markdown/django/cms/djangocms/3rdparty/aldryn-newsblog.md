## install

- [Installation and set-up](http://aldryn-newsblog.readthedocs.io/en/latest/introduction.html#manual-installation)
- [etianen/django-reversion](https://github.com/etianen/django-reversion)
- [aldryn/aldryn-apphooks-config](https://github.com/aldryn/aldryn-apphooks-config)
- [aldryn/aldryn-categories](https://github.com/aldryn/aldryn-categories)
- [aldryn/aldryn-common](https://github.com/aldryn/aldryn-common)
- [aldryn/aldryn-people](https://github.com/aldryn/aldryn-people)
- [aldryn/aldryn-reversion](https://github.com/aldryn/aldryn-reversion)
- [aldryn/aldryn-translation-tools](https://github.com/aldryn/aldryn-translation-tools)


~~~bash
$ pip install aldryn-newsblog

Collecting aldryn-newsblog
  Downloading aldryn-newsblog-1.3.3.tar.gz (273kB)
    100% |████████████████████████████████| 276kB 2.4MB/s
Collecting Django<1.10,>=1.6 (from aldryn-newsblog)
  Downloading Django-1.9.13-py2.py3-none-any.whl (6.6MB)
    100% |████████████████████████████████| 6.6MB 305kB/s
Requirement already satisfied: python-dateutil in /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/lib/python3.6/site-packages (from aldryn-newsblog)
Collecting aldryn-apphooks-config>=0.2.4 (from aldryn-newsblog)
  Downloading aldryn_apphooks_config-0.3.3-py2.py3-none-any.whl
Collecting aldryn-boilerplates>=0.7.2 (from aldryn-newsblog)
  Downloading aldryn-boilerplates-0.7.5.tar.gz
Collecting aldryn-categories (from aldryn-newsblog)
  Downloading aldryn-categories-1.1.0.tar.gz
Collecting aldryn-common>=0.1.3 (from aldryn-newsblog)
  Downloading aldryn-common-1.0.4.tar.gz
Collecting aldryn-people>=1.1.0 (from aldryn-newsblog)
  Downloading aldryn-people-1.2.2.tar.gz (52kB)
    100% |████████████████████████████████| 61kB 9.2MB/s
Collecting aldryn-reversion>=0.1.0 (from aldryn-newsblog)
  Downloading aldryn-reversion-1.1.0.tar.gz
Collecting aldryn-translation-tools>=0.2.0 (from aldryn-newsblog)
  Downloading aldryn-translation-tools-0.2.1.tar.gz
Collecting backport_collections==0.1 (from aldryn-newsblog)
  Downloading backport_collections-0.1.tar.gz
Collecting django-appdata>=0.1.4 (from aldryn-newsblog)
  Downloading django-appdata-0.1.6.tar.gz
Requirement already satisfied: django-cms>=3.2 in /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/lib/python3.6/site-packages (from aldryn-newsblog)
Requirement already satisfied: djangocms-text-ckeditor in /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/lib/python3.6/site-packages (from aldryn-newsblog)
Requirement already satisfied: django-filer>=0.9.9 in /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/lib/python3.6/site-packages (from aldryn-newsblog)
Collecting django-parler>=1.4 (from aldryn-newsblog)
  Downloading django_parler-1.8-py2.py3-none-any.whl (81kB)
    100% |████████████████████████████████| 81kB 4.6MB/s
Collecting django-reversion<1.11,>=1.8.2 (from aldryn-newsblog)
  Downloading django-reversion-1.10.2.tar.gz (67kB)
    100% |████████████████████████████████| 71kB 4.9MB/s
Collecting django-sortedm2m!=1.3.0,!=1.3.1,>=1.2.2 (from aldryn-newsblog)
  Downloading django-sortedm2m-1.5.0.tar.gz
Requirement already satisfied: django-taggit in /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/lib/python3.6/site-packages (from aldryn-newsblog)
Collecting lxml (from aldryn-newsblog)
  Downloading lxml-3.8.0-cp36-cp36m-manylinux1_x86_64.whl (7.3MB)
    100% |████████████████████████████████| 7.3MB 290kB/s
Requirement already satisfied: pytz in /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/lib/python3.6/site-packages (from aldryn-newsblog)
Requirement already satisfied: six in /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/lib/python3.6/site-packages (from aldryn-newsblog)
Collecting YURL>=0.13 (from aldryn-boilerplates>=0.7.2->aldryn-newsblog)
  Downloading YURL-0.13.tar.gz
Requirement already satisfied: django-appconf in /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/lib/python3.6/site-packages (from aldryn-boilerplates>=0.7.2->aldryn-newsblog)
Requirement already satisfied: django-treebeard>=2.0 in /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/lib/python3.6/site-packages (from aldryn-categories->aldryn-newsblog)
Requirement already satisfied: easy-thumbnails in /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/lib/python3.6/site-packages (from aldryn-people>=1.1.0->aldryn-newsblog)
Collecting phonenumbers (from aldryn-people>=1.1.0->aldryn-newsblog)
  Downloading phonenumbers-8.8.0-py2.py3-none-any.whl (2.7MB)
    100% |████████████████████████████████| 2.7MB 747kB/s
Collecting django-phonenumber-field>=0.7.2 (from aldryn-people>=1.1.0->aldryn-newsblog)
  Downloading django-phonenumber-field-1.3.0.tar.gz
Requirement already satisfied: Unidecode<=0.5,>=0.4.18 in /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/lib/python3.6/site-packages (from aldryn-translation-tools>=0.2.0->aldryn-newsblog)
Collecting python-slugify<=1.2,>=1.1.4 (from aldryn-translation-tools>=0.2.0->aldryn-newsblog)
  Downloading python-slugify-1.2.0.tar.gz
Requirement already satisfied: django-classy-tags>=0.7.2 in /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/lib/python3.6/site-packages (from django-cms>=3.2->aldryn-newsblog)
Requirement already satisfied: django-formtools>=1.0 in /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/lib/python3.6/site-packages (from django-cms>=3.2->aldryn-newsblog)
Requirement already satisfied: djangocms-admin-style>=1.0 in /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/lib/python3.6/site-packages (from django-cms>=3.2->aldryn-newsblog)
Requirement already satisfied: django-sekizai>=0.7 in /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/lib/python3.6/site-packages (from django-cms>=3.2->aldryn-newsblog)
Requirement already satisfied: html5lib!=0.9999,!=0.99999,<0.99999999,>=0.90 in /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/lib/python3.6/site-packages (from djangocms-text-ckeditor->aldryn-newsblog)
Requirement already satisfied: Pillow in /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/lib/python3.6/site-packages (from djangocms-text-ckeditor->aldryn-newsblog)
Requirement already satisfied: django-mptt<0.9,>=0.6 in /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/lib/python3.6/site-packages (from django-filer>=0.9.9->aldryn-newsblog)
Requirement already satisfied: django_polymorphic<1.1,>=0.7 in /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/lib/python3.6/site-packages (from django-filer>=0.9.9->aldryn-newsblog)
Requirement already satisfied: babel in /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/lib/python3.6/site-packages (from django-phonenumber-field>=0.7.2->aldryn-people>=1.1.0->aldryn-newsblog)
Collecting phonenumberslite>=7.0.2 (from django-phonenumber-field>=0.7.2->aldryn-people>=1.1.0->aldryn-newsblog)
  Downloading phonenumberslite-8.8.0-py2.py3-none-any.whl (2.7MB)
    100% |████████████████████████████████| 2.7MB 696kB/s
Requirement already satisfied: olefile in /home/vagrant/.anyenv/envs/pyenv/versions/3.6.2/envs/p3_6_2/lib/python3.6/site-packages (from Pillow->djangocms-text-ckeditor->aldryn-newsblog)
Installing collected packages: Django, django-appdata, aldryn-apphooks-config, YURL, aldryn-boilerplates, django-parler, python-slugify, aldryn-translation-tools, aldryn-categories, django-sortedm2m, aldryn-common, django-reversion, aldryn-reversion, phonenumbers, phonenumberslite, django-phonenumber-field, aldryn-people, backport-collections, lxml, aldryn-newsblog
  Found existing installation: Django 1.10.7
    Uninstalling Django-1.10.7:
      Successfully uninstalled Django-1.10.7
  Running setup.py install for django-appdata ... done
  Running setup.py install for YURL ... done
  Running setup.py install for aldryn-boilerplates ... done
  Running setup.py install for python-slugify ... done
  Running setup.py install for aldryn-translation-tools ... done
  Running setup.py install for aldryn-categories ... done
  Running setup.py install for django-sortedm2m ... done
  Running setup.py install for aldryn-common ... done
  Running setup.py install for django-reversion ... done
  Running setup.py install for aldryn-reversion ... done
  Running setup.py install for django-phonenumber-field ... done
  Running setup.py install for aldryn-people ... done
  Running setup.py install for backport-collections ... done
  Running setup.py install for aldryn-newsblog ... done
Successfully installed Django-1.9.13 YURL-0.13 aldryn-apphooks-config-0.3.3 aldryn-boilerplates-0.7.5 aldryn-categories-1.1.0 aldryn-common-1.0.4 aldryn-newsblog-1.3.3 aldryn-people-1.2.2 aldryn-reversion-1.1.0 aldryn-translation-tools-0.2.1 backport-collections-0.1 django-appdata-0.1.6 django-parler-1.8 django-phonenumber-field-1.3.0 django-reversion-1.10.2 django-sortedm2m-1.5.0 lxml-3.8.0 phonenumbers-8.8.0 phonenumberslite-8.8.0 python-slugify-1.2.0
~~~

settings.py:

~~~py
INSTALLED_APPS += [
    'aldryn_apphooks_config',
    'aldryn_categories',
    'aldryn_common',
    'aldryn_newsblog',
    'aldryn_people',
    'aldryn_reversion',
    'aldryn_translation_tools',
    'aldryn_boilerplates',
    'parler',
    'sortedm2m',
    'taggit',
    'reversion',
    ...
]
ALDRYN_BOILERPLATE_NAME = 'bootstrap3'
~~~

migrate:

~~~py
$ python manage.py migrate

Operations to perform:
  Apply all migrations: aldryn_newsblog, easy_thumbnails, filer, djangocms_style, polls, auth, djangocms_link, aldryn_people, djangocms_googlemap, cmsplugin_filer_folder, admin, sessions, contenttypes, reversion, djangocms_video, cms, taggit, cmsplugin_filer_file, polls_cms_integration, cmsplugin_filer_image, sites, djangocms_text_ckeditor, djangocms_snippet, menus, aldryn_categories, djangocms_column
Running migrations:
  Rendering model states... DONE
  Applying aldryn_categories.0001_initial... OK
  Applying aldryn_categories.0002_auto_20150109_1415... OK
  Applying aldryn_categories.0003_auto_20150128_1359... OK
  Applying aldryn_categories.0004_auto_20150623_0859... OK
  Applying taggit.0001_initial... OK
  Applying aldryn_people.0001_initial... OK
  Applying aldryn_newsblog.0001_initial... OK
  Applying aldryn_newsblog.0002_newsblogconfig_template_prefix... OK
  Applying aldryn_newsblog.0003_auto_20150422_1921... OK
  Applying aldryn_newsblog.0004_auto_20150622_1606... OK
  Applying aldryn_newsblog.0005_auto_20150807_0207... OK
  Applying aldryn_newsblog.0006_auto_20160105_1013... OK
  Applying aldryn_newsblog.0007_default_newsblog_config... OK
  Applying aldryn_newsblog.0008_auto_20160106_1735... OK
  Applying aldryn_newsblog.0009_auto_20160211_1022... OK
  Applying aldryn_newsblog.0010_auto_20160316_0935... OK
  Applying aldryn_newsblog.0011_auto_20160412_1622... OK
  Applying aldryn_newsblog.0012_auto_20160503_1626... OK
  Applying aldryn_newsblog.0013_auto_20160623_1703... OK
  Applying aldryn_newsblog.0014_auto_20160821_1156... OK
  Applying aldryn_newsblog.0015_auto_20161208_0403... OK
  Applying aldryn_people.0002_auto_20150128_1411... OK
  Applying aldryn_people.0003_auto_20150425_2103... OK
  Applying aldryn_people.0004_auto_20150622_1606... OK
  Applying aldryn_people.0005_auto_20150723_1508... OK
  Applying aldryn_people.0006_person_groups... OK
  Applying aldryn_people.0007_copy_group... OK
  Applying aldryn_people.0008_remove_person_group... OK
  Applying aldryn_people.0009_auto_20150724_1654... OK
  Applying aldryn_people.0010_auto_20150724_1654... OK
  Applying aldryn_people.0011_auto_20150724_1900... OK
  Applying aldryn_people.0012_auto_20150728_1114... OK
  Applying aldryn_people.0013_peopleplugin_show_ungrouped... OK
  Applying aldryn_people.0014_auto_20150807_0033... OK
  Applying aldryn_people.0015_m2m_remove_null... OK
  Applying aldryn_people.0016_person_fk_to_one_to_one... OK
  Applying aldryn_people.0017_auto_20160109_1951... OK
  Applying aldryn_people.0018_auto_20160802_1852... OK
  Applying reversion.0001_initial... OK
  Applying reversion.0002_auto_20141216_1509... OK
  Applying taggit.0002_auto_20150616_2121... OK
~~~
