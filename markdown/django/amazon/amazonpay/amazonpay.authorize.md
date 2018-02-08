[Step 6:オーソリ（Authorize）のリクエスト](https://pay.amazon.com/jp/developer/documentation/lpwa/201952140)


## 非同期オーソリ(物販など)

- 商品を配送した段階で請求したい場合は非同期モードを利用します。
- 24時間以上注文を保持する場合はこのモードを利用します。
- なぜならば、Amazonに注文確定した後で、すぐに購入者へ注文完了ページを表示する場合では、最終処理ステータスはリアルタイムで有効ではないからです。
- オーソリが `Declined` ステータスである場合は、トランザクションが失敗したことを購入者に通知する必要があり、Amazon Pay Webサイトで支払方法の更新を要求し、その他の正しい支払い方法を選択してもらうか、失敗した理由コードに基いて注文をキャンセルします。
- 非同期モードは一般的に低いオーソリ失敗率になり、Amazon Payがトランザクションを調査する時間を多く提供します。

### 非同期でのTransactionTimeout値

- TransactionTimeout には最小値5から最大値1440（デフォルト値）分までの値を5の倍数でセットします。
- オーソリがこのタイムリミット内で処理できなかった場合に理由コードを TransactionTimedOutとして失敗します。
- 非同期フローを利用する場合は、AuthorizationStatus レスポンス要素は常にPending がセットされます。
- Amazonによって処理されると、オーソリリクエストの最終ステータスをIPN経由で受け取ります。 （例えば、 `Open` や `Declined` です。）

### 非同期の例

~~~py
from pay_with_amazon.client import PayWithAmazonClient

client = PayWithAmazonClient(
    mws_access_key='YOUR_ACCESS_KEY',
    mws_secret_key='YOUR_SECRET_KEY',
    merchant_id='YOUR_MERCHANT_ID',
    region='jp', currency_code='JPY')

response = client.authorize(
    amazon_order_reference_id='Order Referece ID',
    authorization_reference_id='アプリで生成したID',
    amount='1.00',
    seller_authorization_note='Authorizan note.'
    transaction_timeout=60,     # これが非同期
    capture_now=False)
~~~    
