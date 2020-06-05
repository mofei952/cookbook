#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/10/9 19:26
# @File    : p06_define_decorator_that_takes_optional_argument.py
# @Software: PyCharm

"""带可选参数的装饰器"""

import logging
from functools import partial, wraps


# 要实现一个装饰器既可以不传参数，比如@decorator，又可以传递可选参数，比如@decorator(x, y, z)
def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)

    return wrapper


@logged
def foo():
    print('foo')


@logged(level=logging.CRITICAL, name='test', message='messagetest')
def spam():
    print('spam')


logging.basicConfig(level=logging.DEBUG)
foo()
spam()
