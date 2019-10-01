#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/10/1 14:29
# @File    : p25_creating_cached_instances.py
# @Software: PyCharm

# 创建缓存实例
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p25_creating_cached_instances.html

import logging
import weakref

# 相同参数创建的对象是单例的
a = logging.getLogger('foo')
b = logging.getLogger('bar')
print(a is b)
c = logging.getLogger('foo')
print(a is c)


# 使用一个工厂函数实现这种效果
class Spam:
    def __init__(self, name):
        self.name = name


_spam_cache = weakref.WeakValueDictionary()


def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s


a = get_spam('ff')
b = get_spam('ff')
print(a is b)

# WeakValueDictionary只会保存那些在其它地方还在被使用的实例
# 只要实例不再被使用了，它就从字典中被移除了
a = get_spam('foo')
b = get_spam('bar')
c = get_spam('foo')
print(list(_spam_cache))
del a
print(list(_spam_cache))
del c
print(list(_spam_cache))
del b
print(list(_spam_cache))


# 使用单独的缓存管理器
class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s

    def clear(self):
        self._cache.clear()


class Spam:
    manager = CachedSpamManager()

    def __init__(self, name):
        self.name = name

    def get_spam(name):
        return Spam.manager.get_spam(name)


a = Spam.get_spam('foo')
b = Spam.get_spam('foo')
print(a is b)


# 防止直接实例化对象
class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            temp = Spam._new(name)  # Modified creation
            self._cache[name] = temp
        else:
            temp = self._cache[name]
        return temp

    def clear(self):
        self._cache.clear()


class Spam:
    manager = CachedSpamManager()
    def __init__(self, *args, **kwargs):
        raise RuntimeError("Can't instantiate directly")

    # Alternate constructor
    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name
        return self

    def get_spam(name):
        return Spam.manager.get_spam(name)

a = Spam.get_spam('foo')
b = Spam.get_spam('foo')
print(a is b)
