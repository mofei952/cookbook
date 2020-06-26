"""以编程方式定义类"""

import abc
import operator
import sys
import types


# 使用types.new_class()来初始化新的类对象，需要提供类的名字、父类元组、关键字参数，以及一个用成员变量填充类字典的回调函数。
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


s = Stock('ACME', 50, 91.1)
print(s)
print(s.cost())
print()

# 如果创建的类需要一个不同的元类，可以通过types.new_class()的第三个参数传递给它
Stock = types.new_class('Stock', (), {'metaclass': abc.ABCMeta},
                        lambda ns: ns.update(cls_dict))
Stock.__module__ = __name__
print(type(Stock))
print()


# 第三个参数还可以包含其他的关键字参数，以下两个Spam等价
class Base:
    pass


class MyMeta(type):
    def __new__(cls, name, bases, ns, *, debug=False, typecheck=False):
        pass
        return super().__new__(cls, name, bases, ns)


class Spam(Base, metaclass=MyMeta, debug=True, typecheck=False):
    pass


Spam = types.new_class('Spam', (Base, ), {'metaclass': MyMeta, 'debug': True, 'typecheck': False},
                       lambda ns: ns.update(cls_dict))


# 通用的创建类对象的方法，可以替代collections.namedtuple
def named_tuple(classname, fieldnames):
    cls_dict = {name: property(operator.itemgetter(n))
                for n, name in enumerate(fieldnames)}

    def __new__(cls, *args):
        if len(args) != len(fieldnames):
            raise TypeError('Expected {} arguments'.format(len(fieldnames)))
        return tuple.__new__(cls, args)

    cls_dict['__new__'] = __new__

    cls = types.new_class(classname, (tuple, ), {},
                          lambda ns: ns.update(cls_dict))

    cls.__module__ = sys._getframe(1).f_globals['__name__']
    return cls


Point = named_tuple('Point', ['x', 'y'])
print(Point)
p = Point(4, 5)
print(len(p))
print(p.x, p.y)
# p.x = 2  # AttributeError: can't set attribute
print('%s %s' % p)
a, b = p
print(a, b)


# 使用type函数可以创建元类为type的类对象
Stock = type('Stock', (), cls_dict)
