#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/18 19:33
# @File    : p02_accurate_decimal_calculations.py
# @Software: PyCharm

"""执行精确的浮点数运算"""

import math
from decimal import Decimal, localcontext

# 浮点数的一个普遍问题是它们并不能精确的表示十进制数。 并且，即使是最简单的数学运算也会产生小的误差
a = 4.2
b = 2.1
print(a + b)
print((a + b) == 6.3)

# 如果要更加精确(并能容忍一定的性能损耗)，可以使用 decimal 模块
a = Decimal('4.2')
b = Decimal('2.1')
c = a + b
print(c)
print(c == Decimal('6.3'))

# Decimal 对象会像普通浮点数一样的工作(支持所有的常用数学运算)。
# 打印它们或者在字符串格式化函数中使用它们，看起来跟普通数字没什么两样
print(c)
print('{:>10}'.format(c))

# decimal 模块的一个主要特征是可以控制计算的每一方面，包括数字位数和四舍五入运算。
# 为了这样做，先得创建一个本地上下文并更改它的设置
a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)
with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)
with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)

# 注意下减法删除以及大数和小数的加分运算所带来的影响
nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))  # Notice how 1 disappears

# 利用 math.fsum() 所提供的更精确计算能力来解决
print(math.fsum(nums))

# 在真实世界中很少会要求精确到普通浮点数能提供的17位精度。 因此，计算过程中的那么一点点的误差是被允许的。
# 第二点就是，原生的浮点数计算要快的多-有时候在执行大量运算的时候速度也是非常重要的。
# decimal 模块主要用在涉及到金融的领域，在这类程序中，哪怕是一点小小的误差在计算过程中蔓延都是不允许的。
