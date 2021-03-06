# markdown

- [waylan/Python-Markdown](https://github.com/waylan/Python-Markdown)

~~~bash
$ pip install markdown
.
~~~

## URL をアンカーに変換 (エクステンション)

- [r0wb0t/markdown-urlize](https://github.com/r0wb0t/markdown-urlize)

~~~bash
$ curl https://raw.githubusercontent.com/r0wb0t/markdown-urlize/master/mdx_urlize.py -o core/md/mdx_urlize.py
.
~~~

~~~bash
$ tree -P '*.py' core/md/
core/md/
├── __init__.py
└── mdx_urlize.py
~~~

~~~python
In [1]: import markdown
In [2]: md = markdown.Markdown(extensions=['core.md.mdx_urlize'])
In [3]: md.convert('URL http://github.com')
Out[3]: u'<p>URL <a href="http://github.com">http://github.com</a></p>'

~~~

## py-gfm : GitHub-Flavored Markdown for Python

- [Zopieux/py-gfm](https://github.com/Zopieux/py-gfm)

~~~bash
$ pip install py-gfm
.
~~~

~~~python
In [1]: import markdown
In [2]: from mdx_gfm import GithubFlavoredMarkdownExtension
In [4]: md.convert('GFM https://py-gfm.readthedocs.org/en/latest/')
Out[4]: u'<p>GFM <a href="https://py-gfm.readthedocs.org/en/latest/">https://py-gfm.readthedocs.org/en/latest/</a></p>'
~~~

## django

- [GitHub - neutronX/django-markdownx: Comprehensive Markdown plugin built for Django](https://github.com/neutronX/django-markdownx)
