# S3


- [boto で S3 アップローダー](http://qiita.com/ashikawa/items/b3d342ab17a21853214a)

- [
Heroku上のDjangoアプリで静的ファイルをS3から配信する（前編）](http://orangain.hatenablog.com/entry/django-heroku-s3-part1)

- [Amazon S3 での静的ウェブサイトのホスティング](https://docs.aws.amazon.com/ja_jp/AmazonS3/latest/dev/WebsiteHosting.html)
- [Amazon S3における「フォルダ」という幻想をぶち壊し、その実体を明らかにする](http://dev.classmethod.jp/cloud/aws/amazon-s3-folders/)
- [S3のバケット毎の使用量が欲しいんです](http://dev.classmethod.jp/cloud/aws/sugano-003-s3/)
- [AWS S3 製品の詳細](https://aws.amazon.com/jp/s3/details/)


- [Quick way to list all files in Amazon S3 bucket?](http://stackoverflow.com/questions/3337912/quick-way-to-list-all-files-in-amazon-s3-bucket)

- [S3のアクセスコントロールまとめ
](http://qiita.com/ryo0301/items/791c0a666feeea0a704c)

## Django


- [django-storage Amazon S3](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html)
- [django-queued-storage](http://dj ango-queued-storage.readthedocs.io/en/latest/)(django-storage依存)
- [etianen/django-s3-storage](https://github.com/etianen/django-s3-storage)
- [django-extensions sync_s3](http://django-extensions.readthedocs.io/en/latest/sync_s3.html)
- [django-s3-storageを使う](http://qiita.com/key/items/0a2a3efbdf6f988ae281)
- [Using Amazon S3 to Store your Django Site's Static and Media Files](https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/)

- [How to Store Your Media Files in Amazon S3 Bucket](http://djangotricks.blogspot.jp/2013/12/how-to-store-your-media-files-in-amazon.html)

# pre-signed URL

- [S3 の事前署名付き（期限付き）URL を生成する](https://blog.cloudpack.jp/2014/07/08/aws-s3-url-with-expiration-using-php-ruby/)
- [Boto3でS3のpre-signed URLを生成する](http://dev.classmethod.jp/cloud/aws/generate-pre-signed-url-for-s3-with-boto3/)
- [S3の事前署名付き（期限付き）URLに設定できる期限には上限がある](http://qiita.com/kikuchy/items/223ced22d824bec78e1a)
- [署名付き URL を使用したオブジェクトのアップロード](http://docs.aws.amazon.com/ja_jp/AmazonS3/latest/dev/PresignedUrlUploadObject.html)
- [署名付き URL の使用](http://docs.aws.amazon.com/ja_jp/AmazonCloudFront/latest/DeveloperGuide/private-content-signed-urls.html)

- [オリジンアクセスアイデンティティを使用して Amazon S3 コンテンツへのアクセスを制限する](http://docs.aws.amazon.com/ja_jp/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)

## CORS  

- [CORS](http://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html)
- [CORSまとめ](http://qiita.com/tomoyukilabs/items/81698edd5812ff6acb34)
- [CORS(Cross-Origin Resource Sharing)によるクロスドメイン通信の傾向と対策](http://dev.classmethod.jp/cloud/cors-cross-origin-resource-sharing-cross-domain/)



# CloudFront

- [CloudFront を使用してプライベートコンテンツを供給する](http://docs.aws.amazon.com/ja_jp/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html)

- 署名付き URL
- 署名付き Cookie
- Amazon S3 バケット内のコンテンツを保護することで、ユーザーが CloudFront を介してアクセスできても、Amazon S3 URL を使用して直接アクセスすることはできないように設定できます。

- [Creating Signed URLs for Amazon CloudFront](http://stackoverflow.com/questions/2573919/creating-signed-urls-for-amazon-cloudfront)
- [Amazon's CloudFront streaming signed urls](https://djangosnippets.org/snippets/2175/)
- [How to create a signed cloudfront URL with Python?](http://stackoverflow.com/questions/11270254/how-to-create-a-signed-cloudfront-url-with-python)
- [Amazon CloudFront で HLS動画のプライベートオンデマンド配信を行う方法](http://akiyoko.hatenablog.jp/entry/2015/08/24/192618)
- [CloudFront+S3で署名付きURLでプライベートコンテンツを配信する](http://dev.classmethod.jp/cloud/aws/cf-s3-deliveries-use-signurl/)

- [How to Set Up and Serve Private Content Using S3 and Amazon CloudFront](http://improve.dk/how-to-set-up-and-serve-private-content-using-s3/)

- [署名付き Cookie の使用](http://docs.aws.amazon.com/ja_jp/AmazonCloudFront/latest/DeveloperGuide/private-content-signed-cookies.html#private-content-signed-cookie-misuse)
- [AWS CloudFrontでプライベートコンテンツを配信](http://qiita.com/terapyon/items/ff2dd73bd479fbd44e82)

- [Accessing Private Content in Amazon CloudFront](https://java.awsblog.com/post/Tx1VE22EWFR4H86/Accessing-Private-Content-in-Amazon-CloudFront)
