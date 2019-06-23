#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/23 16:33
# @File    : p09_find_commonalities_in_dicts.py
# @Software: PyCharm

# 查找两字典的相同点（比如相同的键、相同的值等等）
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p09_find_commonalities_in_dicts.html

a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# 为了寻找两个字典的相同点，可以简单的在两字典的 keys() 或者 items() 方法返回结果上执行集合操作
print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())

# 以现有字典构造一个排除几个指定键的新字典，可以利用字典推导来实现
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)

# 键视图对象支持集合操作，可以直接使用键视图对象而不用先将它们转换成一个set。
# 字典的 items() 方法返回一个包含 (键，值) 对的元素视图对象。 这个对象同样也支持集合操作，并且可以被用来查找两个字典有哪些相同的键值对。
# 字典的 values() 并不支持这集合操作因为值视图不能保证所有的值互不相同，这样会导致某些集合操作会出现问题。
# 不过，如果硬要在值上面执行这些集合操作的话，可以先将值集合转换成 set，然后再执行集合运算就行了。
print(set(a.values()) & set(b.values()))