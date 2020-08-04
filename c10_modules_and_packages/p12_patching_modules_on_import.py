""" 导入模块的同时修改模块 """


import importlib
import sys
from collections import defaultdict
from functools import wraps


# 在模块被加载时执行某个动作
_post_import_hooks = defaultdict(list)


class PostImportFinder:
    def __init__(self):
        self._skip = set()

    def find_module(self, fullname, path=None):
        if fullname in self._skip:
            return None
        print('11', fullname)
        self._skip.add(fullname)
        return PostImportLoader(self)


class PostImportLoader:
    def __init__(self, finder):
        self._finder = finder

    def load_module(self, fullname):
        importlib.import_module(fullname)
        module = sys.modules[fullname]
        for func in _post_import_hooks[fullname]:
            func(module)
        self._finder._skip.remove(fullname)
        return module


def when_imported(fullname):
    def decorate(func):
        if fullname in sys.modules:
            func(sys.modules[fullname])
        else:
            _post_import_hooks[fullname].append(func)
        return func
    return decorate


sys.meta_path.insert(0, PostImportFinder())


@when_imported('threading')
def warn_threads(mod):
    print('Threading? Are you crazy?')


import threading


# 在已存在的定义上面添加装饰器
def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return wrapper


@when_imported('math')
def add_logging(mod):
    mod.cos = logged(mod.cos)
    mod.sin = logged(mod.sin)


import math
print(math.sin(1))