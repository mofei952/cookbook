"""以编程方式定义类"""

import types
import abc

# 使用types.new_class()来初始化新的类对象，需要提供


def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price


def cost(self):
    return self.shares * self.price


cls_dict = {
    '__init__': __init__,
    'cost': cost,
}


Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
Stock.__module__ = __name__


# 使用这个类对象
s = Stock('ACME', 50, 91.1)
print(s)
print(s.cost())

# 如果创建的类需要一个不同的元类，可以通过types.new_class()的第三个参数传递给它
Stock = types.new_class('Stock', (), {'metaclass': abc.ABCMeta},
                        lambda ns: ns.update(cls_dict))
Stock.__module__ = __name__
print(type(Stock))
