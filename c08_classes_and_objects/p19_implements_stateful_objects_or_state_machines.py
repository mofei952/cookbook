#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/9/23 21:31
# @File    : p19_implements_stateful_objects_or_state_machines.py
# @Software: PyCharm

"""实现状态对象或者状态机"""

from abc import ABCMeta, abstractmethod


# 在很多程序中，有些对象会根据状态的不同来执行不同的操作
class Connection:
    """普通方案，好多个判断语句，效率低下"""

    def __init__(self):
        self.state = 'CLOSED'

    def read(self):
        if self.state != 'OPEN':
            raise RuntimeError('Not open')
        print('reading')

    def write(self, data):
        if self.state != 'OPEN':
            raise RuntimeError('Not open')
        print('writing')

    def open(self):
        if self.state == 'OPEN':
            raise RuntimeError('Already open')
        self.state = 'OPEN'

    def close(self):
        if self.state == 'CLOSED':
            raise RuntimeError('Already closed')
        self.state = 'CLOSED'


# 更好的办法是为每个状态定义一个对象
class Connection1:
    def __init__(self):
        self.new_state(ClosedConnectionState)

    def new_state(self, newstate):
        self._state = newstate

    def read(self):
        return self._state.read(self)

    def write(self, data):
        return self._state.write(self, data)

    def open(self):
        return self._state.open(self)

    def close(self):
        return self._state.close(self)


class ConnectionState(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def read(conn):
        pass

    @staticmethod
    @abstractmethod
    def write(conn, data):
        pass

    @staticmethod
    @abstractmethod
    def open(conn):
        pass

    @staticmethod
    @abstractmethod
    def close(conn):
        pass


class ClosedConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        raise RuntimeError('Not open')

    @staticmethod
    def write(conn, data):
        raise RuntimeError('Not open')

    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)

    @staticmethod
    def close(conn):
        raise RuntimeError('Already closed')


class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print('reading')

    @staticmethod
    def write(conn, data):
        print('writing')

    @staticmethod
    def open(conn):
        raise RuntimeError('Already open')

    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)


c = Connection1()
print(c._state)
# c.read() # RuntimeError: Not open
c.open()
print(c._state)
c.read()
c.write('aa')
c.close()
print(c._state)

# 如果代码中出现太多的条件判断语句的话，代码就会变得难以维护和阅读。
# 这里的解决方案是将每个状态抽取出来定义成一个类。
