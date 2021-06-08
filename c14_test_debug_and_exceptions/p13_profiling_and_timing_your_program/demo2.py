from timeit import timeit
from contextlib import contextmanager
import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
        return r
    return wrapper


@timethis
def countdown(n):
    while n > 0:
        n -= 1


countdown(10000000)


@contextmanager
def timeblock(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print('{} : {}'.format(label, end - start))


with timeblock('counting'):
    n = 10000000
    while n > 0:
        n -= 1


print(timeit('math.sqrt(2)', 'import math'))
print(timeit('sqrt(2)', 'from math import sqrt', number=10000000))
