#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/12 18:40
# @File    : p14_combine_and_concatenate_strings.py
# @Software: PyCharm

"""合并拼接字符串"""

# 要合并的字符串是在一个序列或者 iterable 中，那么最快的方式就是使用 join() 方法
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))

# 如果仅仅只是合并少数几个字符串，使用加号(+)通常已经足够了
a = 'Is Chicago'
b = 'Not Chicago?'
print(a + ' ' + b)

# 可以使用format实现复杂的格式化
print('{} {}'.format(a, b))

# 两个字面字符串合并时可以不用加号(+)
a = 'Hello' 'World'
print(a)

# 当使用加号(+)操作符去连接大量的字符串的时候是非常低效率的，
# 因为加号连接会引起内存复制以及垃圾回收操作
# 永远不要像下面这样写字符串连接代码
# s = ''
# for p in parts:
#     s += p

# 一个相对比较聪明的技巧是利用生成器表达式转换数据为字符串的同时合并字符串，比如：
data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))

# 不要进行不必要的字符串连接操作，比如在打印的时候
a, b, c = 'a', 'b', 'c'
print(a + ':' + b + ':' + c)  # Ugly
print(':'.join([a, b, c]))  # Still ugly
print(a, b, c, sep=':')  # Better


# 当混合使用I/O操作和字符串连接操作的时候，有时候需要仔细研究你的程序，考虑下面的两端代码片段
# Version 1 (string concatenation)
# f.write(chunk1 + chunk2)
# Version 2 (separate I/O operations)
# f.write(chunk1)
# f.write(chunk2)

# 如果两个字符串很小，那么第一个版本性能会更好些，因为I/O系统调用天生就慢。
# 另外一方面，如果两个字符串很大，那么第二个版本可能会更加高效，
# 因为它避免了创建一个很大的临时结果并且要复制大量的内存块数据


# 如果编写构建大量小字符串的输出代码， 最好考虑下使用生成器函数
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


# 可以简单的使用join将生成器返回的字符串合并
text = ''.join(sample())
print(text)


# 也可以重定向到io
# for part in sample():
#     f.write(part)

# 结合I/O操作的混合方案
def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)


with open('p14.txt', 'w') as f:
    for part in combine(sample(), 32768):
        f.write(part)
