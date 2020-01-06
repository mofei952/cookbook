#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/15 19:37
# @File    : p12_iterate_on_items_in_separate_containers.py
# @Software: PyCharm

"""不同集合上元素的迭代"""

from itertools import chain

# 使用itertools.chain()
a = [1, 2, 3, 4]
b = ['a', 'b', 'c']
for i in chain(a, b):
    print(i)

# itertools.chain() 接受一个或多个可迭代对象作为输入参数。然后创建一个迭代器，依次连续的返回每个可迭代对象中的元素。
# 这种方式要比先将序列合并再迭代要高效的多。

# a + b 操作会创建一个全新的序列并要求a和b的类型一致。
# chian() 不会有这一步，所以如果输入序列非常大的时候会很省内存，并且当可迭代对象类型不一样的时候 chain() 同样可以很好的工作。
