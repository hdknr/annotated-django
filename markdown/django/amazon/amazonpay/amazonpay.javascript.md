## [Login with Amazon SDK for JavaScript Reference Guide](https://developer.amazon.com/ja/docs/login-with-amazon/javascript-sdk-reference.html)

### [authorize](https://developer.amazon.com/ja/docs/login-with-amazon/javascript-sdk-reference.html#authorize)

Grant を querysetring で渡す場合:

~~~js
options = { scope: 'profile' };
amazon.Login.authorize(options, 'https://example.org/redirect_here')
~~~

Grant を Javascript で処理する場合

~~~js
options = { scope: 'profile' };
amazon.Login.authorize(options, function(response) {
  if ( response.error ) {
      alert('oauth error ' + response.error);
     return;
  }
alert('success: ' + response.access_token);
});
~~~
