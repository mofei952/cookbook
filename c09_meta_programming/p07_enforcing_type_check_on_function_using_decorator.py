#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/10/14 18:59
# @File    : p07_enforcing_type_check_on_function_using_decorator.py
# @Software: PyCharm

# 利用装饰器强制函数上的类型检查

from inspect import signature
from functools import wraps


# 使用装饰器技术来实现 @typeassert
def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError('Argument {} must be {}'.format(name, bound_types[name]))
            return func(*args, **kwargs)

        return wrapper

    return decorate


# 可以指定所有参数类型，也可以指定部分
@typeassert(int)
def spam(x, y):
    print(x + y)


spam(1, 2)
# spam(2.5, 2.5) # TypeError: Argument x must be <class 'int'>


# 这个方案对于参数的默认值并不会进行检查
@typeassert(int, list)
def bar(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items


bar(2)
# bar(2, 3) # TypeError: Argument items must be <class 'list'>
bar(2, [1, 2, 3])
