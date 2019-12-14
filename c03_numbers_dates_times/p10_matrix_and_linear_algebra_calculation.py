#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/27 18:37
# @File    : p10_matrix_and_linear_algebra_calculation.py
# @Software: PyCharm

"""矩阵与线性代数运算"""

import numpy as np

# 使用NumPy的矩阵对象
m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print(m)

# 转置矩阵
print(m.T)

# 逆矩阵
print(m.I)

# 矩阵相乘
v = np.matrix([[2], [3], [4]])
print(v)
print(m * v)

# numpy.linalg 子包中有更多的操作函数
# 矩阵的行列式
print(np.linalg.det(m))

# 矩阵的特征值
print(np.linalg.eigvals(m))

# mx = v方程中x的解
x = np.linalg.solve(m, v)
print(x)
print(m * x)
print(v)
