## 累積和

~~~py
In [1]: a = [ i + 1 for i in range(10)]

In [2]: a
Out[2]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

In [3]: [sum(i) for i in [a[:i+1] for i in range(len(a))]]
Out[3]: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
~~~
