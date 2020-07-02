"""定义上下文管理器的简单方法"""


import sys
import time
from contextlib import contextmanager
from functools import partial, wraps


# 实现一个新的上下文管理器的最简单方式就是使用contextlib模块中的contextmanager
@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f'{label}: {end - start}')


with timethis('counting') as a:
    n = 10000000
    while n > 0:
        n -= 1


# 自己实现一个contextmanager方法，参考了contextlib模块
class GeneratorContextManager:
    def __init__(self, func, *args, **kwargs):
        self.gen = func(*args, **kwargs)

    def __enter__(self):
        return next(self.gen)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is None:
            try:
                next(self.gen)
            except StopIteration:
                return False
            else:
                raise RuntimeError("generator didn't stop")
        else:
            try:
                self.gen.throw(exc_type, exc_value, exc_traceback)
            except Exception as e:
                if sys.exc_info()[1] is exc_value:
                    return False
                raise


def contextmanager2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return GeneratorContextManager(func, *args, **kwargs)
    return wrapper


@contextmanager2
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f'{label}: {end - start}')


with timethis('counting') as a:
    n = 10000000
    while n > 0:
        n -= 1


# 更加高级一点的上下文管理器，实现了列表对象上的某种事务，对列表的修改只有当不出现异常时才会生效
@contextmanager
def list_tracnsaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working


items = [1, 2, 3]
with list_tracnsaction(items) as working:
    working.append(4)
    working.append(5)
print(items)

try:
    with list_tracnsaction(items) as working:
        working.append(6)
        working.append(7)
        raise RuntimeError('fail')
except Exception as e:
    print(e)
print(items)
