from inspect import signature
import logging

"""在类上强制使用编程规约"""


# 如果想监控类的定义，通常可以通过定义一个元类。
# 一个基本元类通常是继承自type并重定义它的__new__()方法或者是__init__()方法。
class MyMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        return super().__new__(cls, clsname, bases, clsdict)


class MyMeta2(type):
    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)


# 为了使用这个元类，通常要将它放到一个顶级父类定义中，然后其他的类继承这个顶级父类。
class Root(metaclass=MyMeta):
    pass


class A(Root):
    pass


class B(Root):
    pass


# 下面定义了一个元类，它会拒绝任何有混合大小写名字作为方法的类定义
class NoMixedCaseMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError('Bad attribute name: ' + name)
        return super().__new__(cls, clsname, bases, clsdict)


class Root(metaclass=NoMixedCaseMeta):
    pass


class A(Root):
    def foo_bar(self):
        pass


# class B(Root):  # TypeError: Bad attribute name: fooBar
#     def fooBar(self):
#         pass


# 下面的元类用来检测重载方法，确保它的调用参数跟父类中的原始方法有着相同的参数签名
class MatchSignaturesMeta(type):
    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        sup = super(self, self)
        for name, value in clsdict.items():
            if name.startswith('_') or not callable(value):
                continue
            prev_dfn = getattr(sup, name, None)
            if prev_dfn:
                prev_sig = signature(prev_dfn)
                val_sig = signature(value)
                if prev_sig != val_sig:
                    logging.warning(
                        f'Signature mismatch in {value.__qualname__}. {prev_sig} != {val_sig}')


class Root(metaclass=MatchSignaturesMeta):
    pass


class A(Root):
    def foo(self, x, y):
        pass

    def spam(self, x, *, z):
        pass


class B(A):
    def foo(self, a, b):
        pass

    def spam(self, x, z):
        pass


# 在元类中选择重新定义 __new__() 方法还是 __init__() 方法取决于想怎样使用结果类。
# __new__() 方法在类创建之前被调用，通常用于通过某种方式（比如通过改变类字典的内容）修改类的定义。
# 而 __init__() 方法是在类被创建之后被调用，当需要完整构建类对象的时候会很有用。在最后一个例子中，这是必要的，因为它使用了 super() 函数来搜索之前的定义。 它只能在类的实例被创建之后，并且相应的方法解析顺序也已经被设置好了。
