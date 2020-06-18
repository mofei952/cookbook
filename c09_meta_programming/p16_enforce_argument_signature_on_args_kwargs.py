"""*args和**kwargs的强制参数签名"""

import inspect
from inspect import Signature, Parameter


# 有一个函数或方法，它使用*args和**kwargs作为参数，这样使得它比较通用。
# 可以使用inspect模块来检查传递进来的参数是不是想要的类型。
params = [
    Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
    Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
    Parameter('z', Parameter.KEYWORD_ONLY, default=None)
]
sig = Signature(params)
print(sig)


def func(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print(name, value)


func(1, 2, z=3)
print()
func(1)
print()
func(y=2, x=1)
print()
# func(1, x=1)  # TypeError: multiple values for argument 'x'
# func(1, 2, 3)  # TypeError: too many positional arguments


# 强制函数签名具体的例子
def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
             for name in names]
    return Signature(parms)


class Structure:
    __signature__ = make_sig()

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


class Stock(Structure):
    __signature__ = make_sig('name', 'shares', 'price')


class Point(Structure):
    __signature__ = make_sig('x', 'y')


print(inspect.signature(Stock))
s1 = Stock('ACME', 100, 490.1)
# s2 = Stock('ACME', 100)  # TypeError: missing a required argument: 'price'
# s3 = Stock('ACME', 100, 490.1, shares=50)  # # TypeError: multiple values for argument 'shares'
print()


# 自定义元类来创建签名
def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
             for name in names]
    return Signature(parms)


class StructureMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsdict['__signature__'] = make_sig(*clsdict.get('_fields', []))
        return super().__new__(cls, clsname, bases, clsdict)


class Structure(metaclass=StructureMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


class Stock2(Structure):
    _fields = ['name', 'shares', 'price']


class Point2(Structure):
    _fields = ['x', 'y']


# 将签名存储在特定的属性 __signature__ 中通常是很有用的。
# 这样的话，在使用 inspect 模块执行内省的代码就能发现签名并将它作为调用约定。
print(inspect.signature(Stock2))
print(inspect.signature(Point2))
