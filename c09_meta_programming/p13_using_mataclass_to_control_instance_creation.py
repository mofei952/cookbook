#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/10/30 21:37
# @File    : p13_using_mataclass_to_control_instance_creation.py
# @Software: PyCharm

# 使用元类控制实例的创建

# 使用元类定义一个不能直接实例化的类
class NoInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")


class Spam(metaclass=NoInstance):
    @staticmethod
    def grok(self):
        print('Spam.grok')


# spam = Spam()  # TypeError: Can't instantiate directly


# 使用元类实现单例模式
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')


a = Spam()
b = Spam()
print(b is a)
