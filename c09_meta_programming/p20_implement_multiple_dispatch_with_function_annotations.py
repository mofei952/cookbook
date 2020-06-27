"""利用函数注解实现方法重载"""


import inspect
import types
import time


# Python的参数注解
class Spam:
    def bar(self, x: int, y: int):
        print('Bar 1:', x, y)

    def bar(self, s: str, n: int = 0):
        print('Bar 2:', s, n)


s = Spam()
s.bar(2, 3)  # Prints Bar 1: 2 3
s.bar('hello')  # Prints Bar 2: hello 0
print()


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


class MutipleMeta(type):
    '''Metaclass that allows multiple dispatch of methods'''
    def __new__(cls, clsname, bases, clsdict):
        return type.__new__(cls, clsname, bases, dict(clsdict))

    @classmethod
    def __prepare__(cls, name, bases):
        return MutiDict()


class Spam(metaclass=MutipleMeta):
    def bar(self, x: int, y: int):
        print('Bar 1:', x, y)

    def bar(self, s: str, n: int = 0):
        print('Bar 2:', s, n)


class Date(metaclass=MutipleMeta):
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day

    def __init__(self):
        t = time.localtime()
        self.__init__(t.tm_year, t.tm_mon, t.tm_mday)

    def __str__(self):
        return f'{self.__class__} {self.year:04d} {self.month:02d} {self.day:02d}'
        # return '{} {:04d}-{:02d}-{:02d}'.format(self.__class__, self.year, self.month, self.day)


s = Spam()
s.bar(2, 3)
s.bar('hello')
s.bar('hello', 5)
# s.bar(2, 'hello')  # TypeError: No matching method for types (<class 'int'>, <class 'str'>)

d = Date(2012, 12, 21)
print(d)
e = Date()
print(e.year, e.month, e.day)
