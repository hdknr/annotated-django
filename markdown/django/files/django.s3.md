- [django-storage: S3](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html)
- [DjangoでファイルストレージにAmazon S3を使う](http://source.hatenadiary.jp/entry/2013/02/18/190409)
- [DjangoでアップロードファイルをS3に置くときの設定メモ](http://y0m0r.hateblo.jp/entry/20121022/1350916813)

- [Using Amazon S3 to Store your Django Site's Static and Media Files](https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/)

- http://stackoverflow.com/questions/10854095/boto-exception-s3responseerror-s3responseerror-403-forbidden

media, static を別のバケットURLに:

- [jamstooks/django-s3-folder-storage](https://github.com/jamstooks/django-s3-folder-storage)


## S3

- [ポリシーでのアクセス許可の指定](http://docs.aws.amazon.com/ja_jp/AmazonS3/latest/dev/using-with-s3-actions.html)
- [What permissions does django-storages require for an s3 IAM user?](http://stackoverflow.com/questions/12961910/what-permissions-does-django-storages-require-for-an-s3-iam-user)
- [Amazon S3バケットに読み取り専用のポリシーをつけたAWS IAMポリシーをサクッと作る方法](http://dev.classmethod.jp/cloud/aws/iam-group-policy-for-s3-bucket-control/)

~~~json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "AddPerm",
			"Effect": "Allow",
			"Principal": "*",
			"Action": "s3:GetObject",
			"Resource": "arn:aws:s3:::mybucket/static/*"
		},
		{
			"Sid": "AddPerm",
			"Effect": "Allow",
			"Principal": "*",
			"Action": "s3:GetObject",
			"Resource": "arn:aws:s3:::mybucket/media/public/*"
		}
	]
}
~~~


## django-storages

### AWS_DEFAULT_ACL

- [デフォルトは `public-read`](https://bitbucket.org/david/django-storages/src/f153a70ba254dc129d9403546809a02256ef75b5/storages/backends/s3.py?at=default&fileviewer=file-view-default#s3.py-24)

- `private` にして必要なパスに対して `s3:GetObject` を `Allow` する
