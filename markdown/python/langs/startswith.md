# startswith

## PHP

- [PHPでStartsWith/EndsWith - Qiita](https://qiita.com/satoshi-nishinaka/items/f15ccbcf8b8f91c1e2dd)

~~~php
    function startsWith($str, $prefix) {
        return substr($str,  0, strlen($prefix)) === $prefix;
    }
~~~
