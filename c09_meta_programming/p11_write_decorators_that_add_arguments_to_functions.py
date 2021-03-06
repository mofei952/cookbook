#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/10/28 21:40
# @File    : p11_write_decorators_that_add_arguments_to_functions.py
# @Software: PyCharm

"""装饰器为被包装函数增加参数"""

import inspect
from functools import wraps


# 在装饰器中可以使用关键字参数给被包装函数增加额外的参数
def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)

    return wrapper


@optional_debug
def spam(a, b, c):
    print(a, b, c)


spam(1, 2, 3)
spam(1, 2, 3, debug=True)
print()


# 被包装函数参数可能已有debug参数，可能会导致名字冲突，这里增加一步关键字的名字检查
def optional_debug(func):
    if 'debug' in inspect.signature(func).parameters:
        raise TypeError('debug argument already defined')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)

    return wrapper


# 包装后的函数签名其实是错误的，可以修改包装后的函数签名来正确显示
@optional_debug
def spam(a, b, c):
    print(a, b, c)


print(inspect.signature(spam))


def optional_debug(func):
    if 'debug' in inspect.signature(func).parameters:
        raise TypeError('debug argument already defined')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)

    sig = inspect.signature(func)
    params = list(sig.parameters.values())
    params.append(inspect.Parameter(
        'debug', inspect.Parameter.KEYWORD_ONLY, default=False))
    wrapper.__signature__ = sig.replace(parameters=params)
    return wrapper


@optional_debug
def spam(a, b, c):
    print(a, b, c)


print(inspect.signature(spam))
