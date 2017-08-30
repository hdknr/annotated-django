## settings.MIDDLEWARE

~~~py
In [2]: settings.MIDDLEWARE
Out[2]:
['cms.middleware.utils.ApphookReloadMiddleware',
 'django.contrib.sessions.middleware.SessionMiddleware',
 'django.middleware.csrf.CsrfViewMiddleware',
 'django.contrib.auth.middleware.AuthenticationMiddleware',
 'django.contrib.messages.middleware.MessageMiddleware',
 'django.middleware.locale.LocaleMiddleware',
 'django.middleware.common.CommonMiddleware',
 'django.middleware.clickjacking.XFrameOptionsMiddleware',
 'cms.middleware.user.CurrentUserMiddleware',
 'cms.middleware.page.CurrentPageMiddleware',
 'cms.middleware.toolbar.ToolbarMiddleware',
 'cms.middleware.language.LanguageCookieMiddleware']
~~~


## 必須

- 'django.middleware.locale.LocaleMiddleware'
- 'cms.middleware.user.CurrentUserMiddleware'
- 'cms.middleware.page.CurrentPageMiddleware'
- 'cms.middleware.toolbar.ToolbarMiddleware'
- 'cms.middleware.language.LanguageCookieMiddleware'
