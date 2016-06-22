## 配列の配列を平坦化

- [Making a flat list out of list of lists in Python [duplicate]](http://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python)

~~~python
In [9]: import itertools

In [10]: list2d = [[1,2,3],[4,5,6], [7], [8,9]]

In [11]: list(itertools.chain(*list2d))
Out[11]: [1, 2, 3, 4, 5, 6, 7, 8, 9]
~~~
