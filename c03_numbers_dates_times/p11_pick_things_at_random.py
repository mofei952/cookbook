#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/31 19:34
# @File    : p11_pick_things_at_random.py
# @Software: PyCharm

"""随机选择"""

import random

# 使用 random.choice() 从一个序列中随机的抽取一个元素
values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))

# 使用 random.sample() 提取出N个不同元素的样本
print(random.sample(values, 2))
print(random.sample(values, 2))
print(random.sample(values, 3))
print(random.sample(values, 3))

# 打乱序列中元素的顺序
random.shuffle(values)
print(values)

# 使用 random.randint() 生成随机整数
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))
print(random.randint(0, 10))

# 使用 random.random() 生成0到1范围内均匀分布的浮点数
print(random.random())
print(random.random())

# 使用 random.getrandbits() 获取N位二进制的整数
print(random.getrandbits(2))
print(random.getrandbits(200))

# 修改初始化种子
# random.seed() # Seed based on system time or os.urandom()
# random.seed(12345) # Seed based on integer given
# random.seed(b'bytedata') # Seed based on byte data

# 均匀分布随机数
print(random.uniform(1, 2))

# 正态分布随机数
print(random.gauss(0, 1))

# 在 random 模块中的函数不应该用在和密码学相关的程序中。
# 如果确实需要类似的功能，可以使用ssl模块中相应的函数。
# 比如ssl.RAND_bytes()可以用来生成一个安全的随机字节序列。
