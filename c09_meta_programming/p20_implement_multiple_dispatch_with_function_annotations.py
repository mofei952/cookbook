"""利用函数注解实现方法重载"""


import inspect
import types
import time


# 使用参数注解
class Spam:
    def bar(self, x: int, y: int):
        print('Bar 1:', x, y)

    def bar(self, s: str, n: int = 0):
        print('Bar 2:', s, n)


s = Spam()
s.bar(2, 3)
s.bar('hello')
print()


# 利用元类和函数注解来实现重载
class MultiMethod:
    '''Represents a single multimethod'''

    def __init__(self, name):
        self._methods = {}
        self.__name__ = name

    def register(self, meth):
        '''Register a new method as a multimethod'''
        sig = inspect.signature(meth)
        types = []
        for name, parm in sig.parameters.items():
            if name == 'self':
                continue
            if parm.annotation is inspect.Parameter.empty:
                raise TypeError(
                    f'Argument {name} must be annotated with a type')
            if not isinstance(parm.annotation, type):
                raise TypeError(f'Argument {name} annotation must be a type')
            if parm.default is not inspect.Parameter.empty:
                self._methods[tuple(types)] = meth
            types.append(parm.annotation)

        self._methods[tuple(types)] = meth

    def __call__(self, *args):
        '''Call a method based on type signature of the arguments'''
        types = tuple(type(arg) for arg in args[1:])
        meth = self._methods.get(types, None)
        if meth:
            return meth(*args)
        else:
            raise TypeError(f'No matching method for types {types}')

    def __get__(self, instance, cls):
        '''Descriptor methid needed to make calls work in a class'''
        if instance is not None:
            return types.MethodType(self, instance)
        else:
            return self


class MutiDict(dict):
    '''Special dictionary to build multiumethods in a metaclass'''

    def __setitem__(self, key, value):
        if key in self:
            current_value = self[key]
            if isinstance(current_value, MultiMethod):
                current_value.register(value)
            else:
                mvalue = MultiMethod(key)
                mvalue.register(current_value)
                mvalue.register(value)
                super().__setitem__(key, mvalue)
        else:
            super().__setitem__(key, value)


class MultipleMeta(type):
    '''Metaclass that allows multiple dispatch of methods'''

    def __new__(cls, clsname, bases, clsdict):
        return type.__new__(cls, clsname, bases, dict(clsdict))

    @classmethod
    def __prepare__(cls, name, bases):
        return MutiDict()


class Spam(metaclass=MultipleMeta):
    def bar(self, x: int, y: int):
        print('Bar 1:', x, y)

    def bar(self, s: str, n: int = 0):
        print('Bar 2:', s, n)


class Date(metaclass=MultipleMeta):
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

    def __init__(self):
        t = time.localtime()
        self.__init__(t.tm_year, t.tm_mon, t.tm_mday)

    def __str__(self):
        return f'{self.year:04d}-{self.month:02d}-{self.day:02d}'
        # return '{:04d}-{:02d}-{:02d}'.format(self.year, self.month, self.day)


s = Spam()
s.bar(2, 3)
s.bar('hello')
s.bar('hello', 5)
# s.bar(2, 'hello')  # TypeError: No matching method for types (<class 'int'>, <class 'str'>)

d = Date(2012, 12, 21)
print(d)
e = Date()
print(e.year, e.month, e.day)
print()

# MultiMethod 类为了能让 MultiMethod 实例在类定义时正确操作，__get__() 是必须得实现的，它被用来构建正确的绑定方法
b = s.bar
print(b)
print(b.__self__)
print(b.__func__)
b(2, 3)
b('hello')
print()

# 这种实现方法还有一些限制，其中过一个是它不能使用关键字参数
# s.bar(x=2, y=3)  # TypeError: __call__() got an unexpected keyword argument 'x'


# 对于继承也有限制，参数的类型必须严格匹配
class A:
    pass


class B(A):
    pass


class C:
    pass


class Spam(metaclass=MultipleMeta):
    def foo(self, x: A):
        print('Foo 1:', x)

    def foo(self, x: C):
        print('Foo 2:', x)


s = Spam()
a = A()
s.foo(a)
c = C()
s.foo(c)
b = B()
# s.foo(b)  # TypeError: No matching method for types (<class '__main__.B'>,)
print()


# 通过描述器也可以实现类似的效果，但是同样有以上两个限制（不支持关键字参数和继承）
class multimethod:
    def __init__(self, func):
        self._methods = {}
        self.__name__ = func.__name__
        self._default = func

    def match(self, *types):
        def register(func):
            ndefaults = len(func.__defaults__) if func.__defaults__ else 0
            for n in range(ndefaults+1):
                self._methods[types[:len(types) - n]] = func
            return self
        return register

    def __call__(self, *args):
        types = tuple(type(arg) for arg in args[1:])
        meth = self._methods.get(types, None)
        if meth:
            return meth(*args)
        else:
            return self._default(*args)

    def __get__(self, instance, cls):
        if instance is not None:
            return types.MethodType(self, instance)
        else:
            return self


class Spam:
    @multimethod
    def bar(self, *args):
        # Default method called if no match
        raise TypeError('No matching method for bar')

    @bar.match(int, int)
    def bar(self, x, y):
        print('Bar 1:', x, y)

    @bar.match(str, int)
    def bar(self, s, n=0):
        print('Bar 2:', s, n)


s = Spam()
s.bar(1, 1)
s.bar('hello')
