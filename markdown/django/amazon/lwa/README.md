## Login with Amazon(LWA)


- [developer.amazon.com](https://developer.amazon.com/ja?)
- [Login with Amazonについて:developer.amazon.com/ja/login-with-amazon](https://developer.amazon.com/ja/login-with-amazon)

## App Console vs. Pay

- https://developer.amazon.com/lwa/sp/overview.html
- [Thread: "Login with Amazon" vs "Login and Pay with Amazon"](https://sellercentral.amazon.com/forums/message.jspa?messageID=3048899)

## Documentation

- [login.amazon.com](https://login.amazon.com/documentation)
- [developer.amazon.com](https://developer.amazon.com/ja/docs/login-with-amazon/documentation-overview.html)

## Python Social Auth(PSA)

-  [Amazon](http://python-social-auth-docs.readthedocs.io/en/latest/backends/amazon.html)
- [source](https://github.com/python-social-auth/social-core/blob/master/social_core/backends/amazon.py)

Codeフローでのトークンレスポンス([scope=profile](https://developer.amazon.com/ja/docs/login-with-amazon/customer-profile.html#profile)):

~~~py
In [5]: res.keys()
Out[5]: dict_keys(['access_token', 'refresh_token', 'token_type', 'expires_in', 'user_id', 'name', 'email'])
~~~

- ちなみに、　`profile`, `profile:user_id`, `postal_code` の [３つの scope があります](https://developer.amazon.com/ja/docs/login-with-amazon/customer-profile.html)
