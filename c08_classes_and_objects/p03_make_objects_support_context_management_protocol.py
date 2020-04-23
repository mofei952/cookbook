#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/9/6 20:22
# @File    : p03_make_objects_support_context_management_protocol.py
# @Software: PyCharm

"""让对象支持上下文管理协议"""

from socket import socket, AF_INET, SOCK_STREAM
from functools import partial


# 要让一个对象兼容 with 语句，需要实现 __enter__() 和 __exit__() 方法
class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None


conn = LazyConnection(('www.python.org', 80))
with conn as s:
    # conn.__enter__() executes: connection open
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    print(resp)
    # conn.__exit__() executes: connection closed


# 使用多个 with 语句来嵌套使用连接
class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.connections.pop().close()


conn = LazyConnection(('www.python.org', 80))
with conn as s1:
    with conn as s2:
        # s1 and s2 are independent sockets
        print(s1, s2)

# 在需要管理一些资源比如文件、网络连接和锁的编程环境中，使用上下文管理器是很普遍的。
# 这些资源的一个主要特征是它们必须被手动的关闭或释放来确保程序的正确运行
# 通过实现 __enter__() 和 __exit__() 方法并使用 with 语句可以很容易的避免这些问题
