#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/31 21:46
# @File    : p03_keep_last_n_items.py
# @Software: PyCharm

"""保留最后 N 个元素"""

import queue
from collections import deque


# 在迭代操作时使用collections.deque保留有限几个元素的历史记录
# 下面的代码在多行上面做简单的文本匹配，并返回匹配所在行的上面N行
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


with open(r'p03.txt') as f:
    for line, prevlines in search(f, 'python', 5):
        for pline in prevlines:
            print(pline, end='')
        print(line, end='')
        print('-' * 20)

# 使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列。
# 当新的元素加入并且这个队列已满的时候， 最老的元素会自动被移除掉
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)  # deque([1, 2, 3], maxlen=3)
q.append(4)
print(q)  # deque([2, 3, 4], maxlen=3)
q.append(5)
print(q)  # deque([3, 4, 5], maxlen=3)

# 如果不设置最大队列大小，那么就会得到一个无限大小队列，
# 可以在队列的两端执行添加和弹出元素的操作
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)  # deque([1, 2, 3])
q.appendleft(4)
print(q)  # deque([4, 1, 2, 3])
q.pop()
print(q)  # deque([4, 1, 2])
q.popleft()
print(q)  # deque([1, 2])

# 在队列两端插入或删除元素时间复杂度都是 O(1) ，
# 区别于列表，在列表的开头插入或删除元素的时间复杂度为 O(N) 。

# deque 新的元素加入并且这个队列已满的时候, 最老的元素会自动被移除掉
# Queue 新的元素加入并且这个队列已满的时候, put的参数block=True则会阻塞，block=False会抛出FULL异常
q = queue.Queue(maxsize=2)
q.put(1)
q.put(2)
print(q.qsize())
# q.put(3, block=False)
