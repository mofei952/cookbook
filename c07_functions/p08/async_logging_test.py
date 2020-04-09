#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/4/7 21:36
# @File    : async_logging_test.py
# @Software: PyCharm

import logging
from functools import partial
from multiprocessing.pool import Pool


def output_result(result, log=None):
    if log is not None:
        log.debug('Got: %r', result)


def add(x, y):
    return x + y


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')
    callback = partial(output_result, log=log)

    p = Pool()
    p.apply_async(add, (3, 4), callback=callback)
    p.apply_async(add, (3, 5), callback=callback)
    p.close()
    p.join()
