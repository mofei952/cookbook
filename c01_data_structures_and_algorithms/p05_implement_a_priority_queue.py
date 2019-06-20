#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/20 20:54
# @File    : p05_implement_a_priority_queue.py
# @Software: PyCharm

# 实现一个优先级队列
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p05_implement_a_priority_queue.html


# 利用heapq实现一个优先级队列
# 使用(-priority, index, item)的原因：
# 1.优先级为负数的目的是使得元素按照优先级从高到低排序
# 2.index的目的，若item本身不可比较且不使用index，在相同优先级时会比较item1>item2就会报错
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


# 第一个pop()操作返回优先级最高的元素
# 如果两个有着相同优先级的元素，pop操作按照它们被插入到队列的顺序返回的。
q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

# 由于push和pop操作时间复杂度为O(log N)，其中N是堆的大小，因此就算是N很大的时候它们运行速度也依旧很快。
# 若在在多个线程中使用同一个队列，那么需要增加适当的锁和信号量机制。
