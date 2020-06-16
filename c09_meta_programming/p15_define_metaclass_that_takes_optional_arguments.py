"""定义有可选参数的元类"""

from abc import ABCMeta, abstractclassmethod


# 在定义类的时候，可以使用`metaclass`关键字参数来指定特定的元类
class IStream(metaclass=ABCMeta):
    @abstractclassmethod
    def read(self, maxsize=None):
        pass

    @abstractclassmethod
    def write(self, data):
        pass


# 在自定义元类中可以提供其他的关键字参数
# 为了使元类支持这些关键字参数，必须确保在 __prepare__() , __new__() 和 __init__() 方法中 都使用强制关键字参数
class MyMeta(type):
    @classmethod
    def __prepare__(cls, name, bases, *, debug=False, synchronize=False):
        pass
        return super().__prepare__(name, bases)

    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        pass
        return super().__new__(cls, name, bases, ns)

    def __init__(self, name, bases, ns, *, debug=False, synchronize=False):
        pass
        super().__init__(name, bases, ns)


class Spam(metaclass=MyMeta, debug=True, synchronize=True):
    pass


# __prepare__() 方法在所有类定义开始执行前首先被调用，用来创建类命名空间。
# __new__() 方法被用来实例化最终的类对象。它在类的主体被执行完后开始执行。
# __init__() 方法最后被调用，用来执行其他的一些初始化工作。
