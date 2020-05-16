#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/5/16 17:30
# @File    : rpc_server.py
# @Software: PyCharm

from socketserver import ThreadingMixIn
from xmlrpc.server import SimpleXMLRPCServer


class ThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass


def add(a, b):
    return a + b


server = ThreadedXMLRPCServer(('localhost', 15000))
server.register_function(add, 'add')
print('listening')
server.serve_forever()
