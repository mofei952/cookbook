#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/25 20:10
# @File    : p14_sort_objects_without_compare_support.py
# @Software: PyCharm

# 排序不支持原生比较的对象
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p14_sort_objects_without_compare_support.html


class User:
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return 'User({})'.format(self.user_id)


# 利用lambda表达式对 User 的 user_id 属性进行排序
users = [User(23, 'a', 'b'), User(3, 'b', 'c'), User(99, 'c', 'a')]
print(sorted(users, key=lambda u: u.user_id))

# 使用 operator.attrgetter()
from operator import attrgetter
print(sorted(users, key=attrgetter('user_id')))

# operator.attrgetter() 允许多个字段进行比较
by_name = sorted(users, key=attrgetter('last_name', 'first_name'))
print(by_name)

# 以上用法适用于像 min() 和 max()
print(min(users, key=attrgetter('user_id')))
print(max(users, key=attrgetter('user_id')))
