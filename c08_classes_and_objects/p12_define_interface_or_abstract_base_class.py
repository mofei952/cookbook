# 定义接口或者抽象基类
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p12_define_interface_or_abstract_base_class.html

import collections
import io
from abc import ABCMeta, abstractmethod


# 使用abc模块定义抽象基类
class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


# 抽象类不能被实例化
# a = IStream()  # TypeError: Can't instantiate abstract class IStream with abstract methods read, write


# 抽象类的目的就是让别的类继承它并实现特定的抽象方法
class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass


# 抽象基类的一个主要用途是在代码中检查某些对象是否为特定类型，实现了特定接口
def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')


# 还可以通过注册方式来让某个类实现抽象基类
IStream.register(io.IOBase)

f = open('p12.txt')
print(isinstance(f, IStream))


# @abstractmethod 还能注解静态方法、类方法和 properties
# 只需保证这个注解紧靠在函数定义前即可
class A(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass


# python标准库中有很多用到抽象基类的地方
print(isinstance([], collections.Sequence))
print(isinstance([], collections.Iterable))
print(isinstance([], collections.Sized))
print(isinstance({}, collections.Mapping))
