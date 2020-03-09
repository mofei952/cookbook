#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/3/4 20:21
# @File    : p21_serializing_python_objects.py
# @Software: PyCharm

"""序列化Python对象"""

import math
import pickle
import threading
import time

# 将对象保存到文件
data = 'dadasd'
f = open('p21', 'wb')
pickle.dump(data, f)

# 将对象转储为字符串
s = pickle.dumps(data)
print(s)

# 从字节流中恢复一个对象
f = open('p21', 'rb')
data = pickle.load(f)
print(data)

data = pickle.loads(s)
print(data)

# 处理多个对象
f = open('p21_2', 'wb')
pickle.dump([1, 2, 3, 4], f)
pickle.dump('hello', f)
pickle.dump({'Apple', 'Pear', 'Banana'}, f)
f.close()
f = open('p21_2', 'rb')
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))

# 可以序列化函数，类，接口，但是结果数据仅仅将它们的名称编码成对应的代码对象
print(pickle.dumps(math.cos))


# 当数据反序列化回来的时候，会先假定所有的源数据时可用的。 模块、类和函数会自动按需导入进来。

# 千万不要对不信任的数据使用pickle.load()。
# pickle在加载时有一个副作用就是它会自动加载相应模块并构造实例对象。
# 但是某个坏人如果知道pickle的工作原理，
# 他就可以创建一个恶意的数据导致Python执行随意指定的系统命令。
# 因此，一定要保证pickle只在相互之间可以认证对方的解析器的内部使用。

# 有些类型的对象是不能被序列化的。
# 这些通常是那些依赖外部系统状态的对象， 比如打开的文件，网络连接，线程，进程，栈帧等等。
# 用户自定义类可以通过提供 __getstate__() 和 __setstate__() 方法来绕过这些限制。

# 下面是一个在内部定义了一个线程但仍然可以序列化和反序列化的类
class Countdown:
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(1)

    def __getstate__(self):
        return self.n

    def __setstate__(self, n):
        self.__init__(n)


# c = Countdown(30)
# time.sleep(5)
# f = open('p21_3', 'wb')
# pickle.dump(c, f)
# f.close()

f = open('p21_3', 'rb')
pickle.load(f)

# 由于 pickle 是Python特有的并且附着在源码上，所有如果需要长期存储数据的时候不应该选用它。
# 例如，如果源码变动了，你所有的存储数据可能会被破坏并且变得不可读取。

# 对于在数据库和存档文件中存储数据时，最好使用更加标准的数据编码格式如XML，CSV或JSON。
# 这些编码格式更标准，可以被不同的语言支持，并且也能很好的适应源码变更。
