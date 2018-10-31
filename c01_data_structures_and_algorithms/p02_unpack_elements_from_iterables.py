#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/26 19:07
# @File    : p02_unpack_elements_from_iterables.py
# @Software: PyCharm

# 解压可迭代对象赋值给多个变量
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p02_unpack_elements_from_iterables.html

# 1.星号表达式
# 除掉第一个和最后一个分数的平均分数
grades = [1, 2, 3, 4, 5]
first, *middle, last = grades
print(sum(middle) / len(middle))  # 3.0

# 不确定数量的电话个数
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(phone_numbers)  # ['773-555-1212', '847-555-1212']

# 当前月销售数据的和前n个月销售数据的平均做对比
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
trailing_avg = sum(trailing) / len(trailing)
print(trailing_avg, current)  # 7.142857142857143 3

# 迭代元素为可变长元组的序列
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]
def do_foo(x, y):
    print('foo', x, y)
def do_bar(s):
    print('bar', s)
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# 字符串分割操作
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

# 有时候需要丢弃一些元素，可以使用一个普通的废弃名称，比如 _ 或者 ign （ignore）
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record

# 巧妙的实现递归算法
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
print(sum([1, 10, 7, 4, 5, 9]))  # 36
