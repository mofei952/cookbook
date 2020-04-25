#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/4/25 17:44
# @File    : p07_calling_method_on_parent_class.py
# @Software: PyCharm

"""调用父类方法"""


# 使用super()函数调用父类的方法
class A:
    def spam(self):
        print('A.spam')


class B(A):
    def spam(self):
        print('B.spam')
        super().spam()


b = B()
b.spam()


# super() 函数的一个常见用法是在 __init__() 方法中确保父类被正确的初始化了
class A:
    def __init__(self):
        self.x = 0


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1


# super() 的另外一个常见用法出现在覆盖Python特殊方法的代码中
# 就算没有显式的指明某个类的父类， super() 仍然可以有效的工作
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)  # Call original __setattr__
        else:
            setattr(self._obj, name, value)


# 每个类都有一个方法解析顺序(MRO)列表，Python会在MRO列表上从左到右开始查找基类
# 这个MRO列表的构造是通过一个C3线性化算法来实现的
class Base:
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')


class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')


class C(A, B):
    def __init__(self):
        super().__init__()
        print('C.__init__')


print(C.mro())
c = C()


# super() 并不一定去查找某个类在MRO中下一个直接父类
class A:
    def spam(self):
        print('A.spam')
        super().spam()


# a = A()
# a.spam()#'super' object has no attribute 'spam'

class B:
    def spam(self):
        print('B.spam')


class C(A, B):
    pass


c = C()
c.spam()
print(C.mro())

# 类A单独使用会报错，但是多继承时可以正常使用
# 在类A中使用 super().spam() 实际上调用的是跟类A毫无关系的类B中的 spam() 方法
# 这个用类C的MRO列表就可以完全解释清楚了


# 由于 super() 可能会调用不是你想要的方法，应该遵循一些通用原则。
# 首先，确保在继承体系中所有相同名字的方法拥有可兼容的参数签名(比如相同的参数个数和参数名称)。这样可以确保 super() 调用一个非直接父类方法时不会出错。
# 其次，最好确保最顶层的类提供了这个方法的实现，这样的话在MRO上面的查找链肯定可以找到某个确定的方法。
