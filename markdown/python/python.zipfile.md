- [12.4. zipfile — ZIP アーカイブの処理](http://docs.python.jp/2/library/zipfile.html#module-zipfile)
- [How do I set permissions (attributes) on a file in a ZIP file using Python's zipfile module?](http://stackoverflow.com/questions/434641/how-do-i-set-permissions-attributes-on-a-file-in-a-zip-file-using-pythons-zip)


## 例

~~~py
@main.command()
@click.argument('id')
@click.argument('path')
@click.pass_context
def archive_activity(ctx, id, path):
    import zipfile
    json = BaseQuerySet(models.Activity).filter(id=id).serialize()
    archive = zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED)
    now = timezone.now()
    inf = zipfile.ZipInfo('archive.json', now.timetuple()[:6])
    inf.external_attr |= 0644 << 16L
    archive.writestr(inf, json)
    archive.close()
~~~    
