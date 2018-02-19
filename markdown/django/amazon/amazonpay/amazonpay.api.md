## API

### [イントロダクション](https://pay.amazon.com/jp/developer/documentation/apireference/201751630)

Billing Agreement:

- 購入者からの配送先情報を取得
- 自動支払のための送料計算
- Amazon Payで毎月請求することが許可された金額の情報を取得
- 自動支払についての説明とその他の情報の設定
- 購入者がサイト上で自動支払を許可した後でBilling Agreementを承認
- 販売事業者または購入者が自動支払の契約を解除する場合はBilling Agreementを終了

Order Reference:

- 購入者から配送先情報を取得し送料計算
- 注文についての金額、説明、その他のオプション情報
- 購入者がWebサイト上で注文完了した後で注文を承認
- 購入者または販売事業者のどちらかが注文のキャンセル
- 注文が処理済みであり完了した後で注文を終了

集金など:
- Webサイトで購入者が、購入するための金額をオーソリ、売上請求、返金することをプログラムで処理します。

### [用語](https://pay.amazon.com/jp/developer/documentation/apireference/201751650)

Billing Agreement オブジェクト:

- 購入者が選択した支払方法、配送先住所、自動支払のAuthorizationを管理します。
- 決まっていない存在期間と購入数を持つことができます。

Order Reference オブジェクト:

- 購入者によって生成されたそれぞれの購入の情報です。
- 購入者が購入に支払に許可した支払方法、配送先住所、金額を管理します。
- 自動支払では、Order ReferenceはBilling Agreementに保存されている配送先と支払情報から生成されます。
- 180日有効であり、１回購入のみに許可されます。
- １つのOrder Referenceは10回までのAuthorizationを持つことができます。

Authorization オブジェクト:

- 資金の有効性を管理
- Order Referenceに保存されている将来の支払方法に対して資金を確保します。

Capture オブジェクト:

- 購入者の支払方法から事前に確保されたAuthorizationの資金を販売事業者のアカウントに移動します。

Refundオブジェクト:

- 以前に販売事業者のアカウントにCaptureされた資金を購入者の支払方法に移動します。

Transaction

- Order Referenceに対して発生する全ての支払イベントで使われる一般的な用語です。
- これには、Authorization、Capture、Refund、マーケットプレイス保証、チャージバック、その他の様々なものが含まれます。

エンドポイント:

- 本番環境 ：https://mws-fe.amazonservice.com/OffAmazonPayments/2013-01-01/
- SANDBOX ：https://mws-fe.amazonservice.com/OffAmazonPayments_Sandbox/2013-01-01/

### メソッド

Order:

  - GetOrderReferenceDetails
  - SetOrderReferenceDetails
  - ConfirmOrderReference
  - CloseOrderReference
  - CancelOrderReference

Auth:

  - Authorize
  - GetAuthorizationDetails
  - CloseAuthorization

Capture:

  - Capture
  - GetCaptureDetails

Refund:

  - Refund
  - GetRefundDetails

Service:

  - GetServiceStatus

## 資料

- [amzn/amazon-pay-sdk-python](https://github.com/amzn/amazon-pay-sdk-python)
- [django-oscar-amazon-payments:models](https://github.com/simonkagwe/django-oscar-amazon-payments/blob/master/amazon_payments/models.py)
