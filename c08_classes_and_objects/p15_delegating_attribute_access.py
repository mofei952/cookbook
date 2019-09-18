#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/9/18 21:21
# @File    : p15_delegating_attribute_access.py
# @Software: PyCharm

# 属性的代理访问
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p15_delegating_attribute_access.html

# 代理是一种编程模式，它将某个操作转移给另外一个对象来实现
class A:
    def spam(self, x):
        pass

    def foo(self):
        pass


class B1:
    """简单的代理"""

    def __init__(self):
        self._a = A()

    def spam(self, x):
        # Delegate to the internal self._a instance
        return self._a.spam(x)

    def foo(self):
        # Delegate to the internal self._a instance
        return self._a.foo()

    def bar(self):
        pass


# 如果有大量的方法需要代理， 那么使用 __getattr__() 方法或许或更好些
class B2:
    """使用__getattr__的代理，代理方法比较多时候"""

    def __init__(self):
        self._a = A()

    def bar(self):
        pass

    # Expose all of the methods defined on class A
    def __getattr__(self, name):
        """这个方法在访问的attribute不存在的时候被调用
        the __getattr__() method is actually a fallback method
        that only gets called when an attribute is not found"""
        return getattr(self._a, name)


# 另外一个代理例子是实现代理模式
# A proxy class that wraps around another object, but
# exposes its public attributes
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        print('getattr:', name)
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print('setattr:', name, value)
            setattr(self._obj, name, value)

    # Delegate attribute deletion
    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print('delattr:', name)
            delattr(self._obj, name)


# 使用代理类包装其他类
class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('Spam.bar:', self.x, y)


s = Spam(1)
p = Proxy(s)
print(p.x)
p.bar(2)


# __getattr__() 对于大部分以双下划线(__)开始和结尾的属性并不适用
class ListLike:
    """__getattr__对于双下划线开始和结尾的方法是不能用的，需要一个个去重定义"""

    def __init__(self):
        self._items = []

    def __getattr__(self, name):
        return getattr(self._items, name)


a = ListLike()
a.append(2)
a.insert(0, 1)
a.sort()
# len(a) # TypeError: object of type 'ListLike' has no len()
# a[0] # TypeError: 'ListLike' object does not support indexing


# 代理类有时候可以作为继承的替代方案
class A:
    def spam(self, x):
        print('A.spam', x)

    def foo(self):
        print('A.foo')


class B(A):
    def spam(self, x):
        print('B.spam')
        super().spam(x)

    def bar(self):
        print('B.bar')


class B:
    def __init__(self):
        self._a = A()

    def spam(self, x):
        print('B.spam', x)
        self._a.spam(x)

    def bar(self):
        print('B.bar')

    def __getattr__(self, name):
        return getattr(self._a, name)
