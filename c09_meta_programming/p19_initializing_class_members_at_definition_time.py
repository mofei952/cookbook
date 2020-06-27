"""在定义的时候初始化类的成员"""


import operator


# 在类定义时就执行初始化或设置操作是元类的一个典型应用场景
class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))


class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []

    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise ValueError(f'{len(cls._fields)} arguments required')
        return super().__new__(cls, args)


class Stock(StructTuple):
    _fields = ['name', 'shares', 'price']


class Point(StructTuple):
    _fileds = ['x', 'y']


s = Stock('ACME', 50, 91.1)
print(s)
print(s[0])
print(s.name)
print(s.shares * s.price)
# s.shares = 23  # AttributeError: can't set attribute
