#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/10/8 21:41
# @File    : p05_define_decorator_with_user_adjustable_attributes.py
# @Software: PyCharm

"""可自定义属性的装饰器"""

import time
from functools import wraps, partial
import logging


# Utility decorator to attach a function as an attribute of obj
def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


# 引入一个访问函数，使用 nonlocal 来修改内部变量。
# 然后这个访问函数被作为一个属性赋值给包装函数
def logged(level, name=None, message=None):
    """
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    """

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        # Attach setter functions
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        @attach_wrapper(wrapper)
        def get_level():
            return level

        return wrapper

    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y


logging.basicConfig(level=logging.DEBUG)
print(add(2, 3))
add.set_message('Add called')
print(add(2, 3))
add.set_level(logging.WARNING)
print(add(2, 3))
print(add.get_level() == logging.WARNING)
print()


# 访问函数会在多层装饰器间传播(如果装饰器都使用了 @functools.wraps 注解)
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
@logged(logging.DEBUG)
def countdown(n):
    while n > 0:
        n -= 1


countdown.set_message('count')
countdown(10000)
print()


# 以下是另一个自定义属性的方法，但前提是它必须是最外层的装饰器才行
def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            wrapper.log.log(wrapper.level, wrapper.logmsg)
            return func(*args, **kwargs)

        wrapper.level = level
        wrapper.logmsg = logmsg
        wrapper.log = log

        return wrapper

    return decorate


@logged(logging.DEBUG)
@timethis
def countdown(n):
    while n > 0:
        n -= 1


countdown.level = logging.ERROR
countdown(10000)
print()


@timethis
@logged(logging.DEBUG)
def countdown(n):
    while n > 0:
        n -= 1


countdown.level = logging.ERROR
countdown(10000)
