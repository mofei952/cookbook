# 调用父类方法
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p07_calling_method_on_parent_class.html


# 使用super()函数调用父类的一个方法
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


# 每个类都有一个方法解析顺序(MRO)列表
# 而这个MRO列表的构造是通过一个C3线性化算法来实现的
# Python会在MRO列表上从左到右开始查找基类
class Base:
    def __init__():
        print('Base.__init__')


class A(Base):
    def __init__():
        super().__init__()
        print('A.__init__')


class B(Base):
    def __init__():
        super().__init__()
        print('B.__init__')


class C(A, B):
    def __init__():
        super().__init__()
        print('C.__init__')


print(C.mro())


# super() 并不一定去查找某个类在MRO中下一个直接父类
# 在类A中使用 super().spam() 实际上调用的是跟类A毫无关系的类B中的 spam() 方法
# 由于 super() 可能会调用不是你想要的方法, 所以应该确保在继承体系中所有相同名字的方法拥有可兼容的参数签名(比如相同的参数个数和参数名称)。
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
