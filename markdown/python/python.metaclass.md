## ドキュメント

- [3.4.3. クラス生成をカスタマイズする](http://docs.python.jp/2/reference/datamodel.html#metaclasses)


## `type()`` 関数

- [class type(name, bases, dict)](http://docs.python.jp/2/library/functions.html#type)

- `name` : `__name__` 属性
- `bases`: 継承する基底クラスを`tuple` で指定
- `dict` : `__dict__` 属性

~~~py
class Person(object):
    ROLE = 'Generic'

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


def get_wage(obj):
    return getattr(obj, 'wage', 0)


Employee = type('EmployeeClass',
                (Person, ),
                {'ROLE': 'Worker', 'get_wage': get_wage})

e = Employee(wage=1500)

print e.ROLE, e.get_wage()
~~~
~~~bash
Worker 1500
~~~


## `__new__()` メソッド

- [`object.__new__(cls[, ...])`](http://docs.python.jp/2/reference/datamodel.html?highlight=__new__#object.__new__)
- static メソッド
- `cls` : 生成される対象のクラス
- `cls以降の引数`: コンストラクタにパススルーされる
- `return` : `cls`のインスタンスobj. この場合、 `obj.__init__(...)` が呼ばれる。もしもべつクラスのインスタンスを返すと、そのクラスの`__init__が呼ばれます`(objが帰らないと`__init__`は呼ばれない)

~~~py
class Employee(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.wage = 100


class Employer(Employee):
    def __init__(self, **kwargs):
        super(Employer, self).__init__(**kwargs)
        self.car = 'BMW'


class Worker(object):
    def __new__(cls, **kwargs):
        return 'vip' in kwargs and Employer(**kwargs) or Employee(**kwargs)

    def __init__(self, **kwargs):
        raise Exception('Never Called')


w = Worker(name='foo', age=35)
print w.name, w.age, w.wage

w = Worker(name='bar', age=45, vip=True)
print w.name, w.age, w.car
~~~

~~~bash
foo 35 100
bar 45 BMW
~~~

## `__metaclass__`

- [`__metaclass__`](http://docs.python.jp/2/reference/datamodel.html#__metaclass__)

- この変数は name 、 bases 、および dict を引数として取るような任意の呼び出し可能オブジェクトにできます。
- クラス生成の際、組み込みの type() の代わりに、指定された呼び出しオブジェクトが呼び出されます。

メタクラス決定優先度:

1. dict['`__metaclass__`']
2. 基底クラスのメタクラス
3. 基底クラス自身
4. グローバル変数`__metaclass__`
5. 旧スタイルのメタクラス (types.ClassType)


~~~py
class Mammalian:                                                                    
    raised_by_milk = True                                                           


class Human(type):                                                                  
    def __new__(cls, classname, baseclasses, attrs):                                
        assert cls == Human                                                         
        attrs['minimum_sleeping_hours'] = 8                                         
        baseclasses += (Mammalian, )                                                
        attrs['classname'] = classname                                              
        # return super(Human, cls).__new__(cls, classname, baseclasses, attrs)   
        return type.__new__(cls, classname, baseclasses, attrs)                     

    def __init__(cls, classname, baseclasses, attrs):                               
        assert cls.__name__ == 'Employee'                                           
        super(Human, cls).__init__(classname, baseclasses, attrs)                   


class Employee(object):                                                             
    __metaclass__ = Human                                                           

    def __init__(self, name, age):                                                  
        self.name = name                                                            
        self.age = age                                                              


e = Employee('Foo', 29)                                                             

print e.name, e.age, e.minimum_sleeping_hours, e.raised_by_milk, e.classname  
~~~

~~~bash
Foo 29 8 True Employee
~~~
