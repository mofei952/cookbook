#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/2 20:06
# @File    : p03_match_strings_with_shell_wildcard.py
# @Software: PyCharm

"""用Shell通配符匹配字符串"""

from fnmatch import fnmatch, fnmatchcase

# 使用fnmatch()
print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])

# fnmatch() 函数使用底层操作系统的大小写敏感规则(不同的系统是不一样的)来匹配模式
# On OS X (Mac)
fnmatch('foo.txt', '*.TXT')  # False
# On Windows
fnmatch('foo.txt', '*.TXT')  # True

# 使用 fnmatchcase() 可以忽略大小写
fnmatchcase('foo.txt', '*.TXT')

# 这两个函数通常会被忽略的一个特性是在处理非文件名的字符串时候它们也是很有用的。
# 比如，假设有一个街道地址的列表数据，可以像这样写列表推导
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])

# fnmatch() 函数匹配能力介于简单的字符串方法和强大的正则表达式之间。
# 如果在数据处理操作中只需要简单的通配符就能完成的时候，这通常是一个比较合理的方案。
# 如果需要做文件名的匹配，最好使用 glob 模块
