import math
import time
from contextlib import contextmanager
from math import sqrt


@contextmanager
def timeblock(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print('{} : {}'.format(label, end - start))


def compute_roots(nums):
    result = []
    for n in nums:
        result.append(math.sqrt(n))
    return result


with timeblock('counting'):
    nums = range(1000000)
    for n in range(100):
        r = compute_roots(nums)


def compute_roots(nums):
    result = []
    result_append = result.append
    for n in nums:
        result_append(sqrt(n))
    return result


with timeblock('counting'):
    nums = range(1000000)
    for n in range(100):
        r = compute_roots(nums)


def compute_roots(nums):
    sqrt = math.sqrt
    result = []
    result_append = result.append
    for n in nums:
        result_append(sqrt(n))
    return result


with timeblock('counting'):
    nums = range(1000000)
    for n in range(100):
        r = compute_roots(nums)
