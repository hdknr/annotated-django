## 公式

- [STEP3 ボタン](https://pay.amazon.com/jp/developer/documentation/lpwa/201952050)

Amazon Pay:

  Amazon Pay = Amazonログイン + Amazon Pay サービス

access token:

- Amazonログイン で認証に成功すると `access token` が返答される

## 1. onAmazonLoginReady + onAmazonPaymentsReady


- [JavaScriptの「WebページにCallbackとwidgets.jsコードの追加」](https://pay.amazon.com/us/developer/documentation/lpwa/201909430)

~~~html
<head>
    <script type='text/javascript'>
        window.onAmazonLoginReady = function() {
          amazon.Login.setClientId('CLIENT-ID');
        };
        window.onAmazonPaymentsReady = function() {
          showButton();     // ボタンを表示させる
        };
    </script>
</head>
~~~

## 2. Widget.js

- 'async' で追加

URL:

- SANDBOX: https://static-fe.payments-amazon.com/OffAmazonPayments/jp/sandbox/lpa/js/Widgets.js
- 本番環境: https://static-fe.payments-amazon.com/OffAmazonPayments/jp/lpa/js/Widgets.js

~~~html
<head>
    <script type='text/javascript'>
        window.onAmazonLoginReady = function() {
          amazon.Login.setClientId('CLIENT-ID');
        };
        window.onAmazonPaymentsReady = function() {
          showButton();
        };
        </script>
        <script async="async"
        src='https://static-na.payments-amazon.com/OffAmazonPayments/us/sandbox/js/Widgets.js'>
    </script>
</head>
~~~

## 3. ボタン

- [ボタンウィジェット](https://pay.amazon.com/jp/developer/documentation/lpwa/201953980)

~~~html
<div id="AmazonPayButton">
</div>
...

<script type="text/javascript">
function showButton() {
    var authRequest;
    OffAmazonPayments.Button(
        "AmazonPayButton",
        " SELLER-ID",
        {type: "TYPE", color: "COLOR", size: "SIZE",
          authorization: function() {
            loginOptions = {scope: "SCOPES", popup: "POPUP-PARAMETER"};
            authRequest = amazon.Login.authorize (loginOptions,"REDIRECT-URL");
          }}
    );
}
</script>
~~~

## 4. エラー処理

- [エラーハンドリング](https://pay.amazon.com/jp/developer/documentation/lpwa/201954960)

~~~js
...
onError: function(error) {
    // your error handling code.
    // alert("The following error occurred: "
    // + error.getErrorCode()
    // + ' - ' + error.getErrorMessage());
}
...
~~~

## 5. ログアウト

~~~html
<script type="text/javascript">
    document.getElementById('Logout').onclick = function() {
        amazon.Login.logout();
    };
</script>
~~~
