## 0. 購入

![](images/addidas/00.1.pickup.png)

エラーチェック:

![](images/addidas/00.2.pickup.error.png)

完了:

![](images/addidas/00.3.pickup.complete.png)

## 1.カート

- https://shop.adidas.jp/pc/secure/cart/recalc.cgi


![](images/addidas/01.cart.png)


## 2. アカウント/支払い選択

カートで `購入手続き` をクリック

- https://shop.adidas.jp/pc/secure/cart/step02l.cgi

![](images/addidas/02.accounts.png)

## 3. ログイン

支払いで、 `Amazonアカウントで支払い` をクリック

![](images/addidas/03.login.popup.png)

2ファクター設定済みアカウント

![](images/addidas/04.login.2factor.png)

## 4.お届け

AuthRes URL(GET+QUERYでいいのか？):

~~~
https://shop.adidas.jp/pc/secure/cart/step02.cgi?
coupon_code=&
cart_view_date=20180122&
access_key_hash=04a****......&
juchKess=8&
juchHflg=2&
amazon_payment_flag=1&
shopId=&
shop_stock=&
access_token=Atza%x**********......*&
token_type=bearer&
expires_in=3600&
scope=profile%20postal_code%20payments%3Awidget%20payments%3Ashipping_address

~~~

![](images/addidas/05.delivery.png)

## 5.カード

- https://shop.adidas.jp/pc/secure/cart/step03.cgi

![](images/addidas/06.payment.png)
