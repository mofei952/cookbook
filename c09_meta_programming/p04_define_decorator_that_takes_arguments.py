#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/10/7 21:28
# @File    : p04_define_decorator_that_takes_arguments.py
# @Software: PyCharm

# 定义一个带参数的装饰器

import logging


def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        return wrapper

    return decorate


@logged(logging.WARNING)
def add(x, y):
    return x + y


# 装饰器处理过程和以下语句是等效的
# add = logged(logging.DEBUG)(add)

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


logging.basicConfig(level=logging.WARNING)
print(add(1, 2))
spam()
