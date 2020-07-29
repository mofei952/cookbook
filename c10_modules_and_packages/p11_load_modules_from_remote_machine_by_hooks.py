import imp
from urllib.request import urlopen
import sys


# 将一些文件作为模块被远程访问
# cd p11
# python -m http.sererver 15000


# 加载远程模块
# 该函数会下载源代码，并使用compile()将其编译到一个代码对象中，然后在一个新创建的模块对象的字典中来执行它。
def load_module(url):
    u = urlopen(url)
    source = u.read().decode('utf-8')
    mod = sys.modules.setdefault(url, imp.new_module(url))
    code = compile(source, url, 'exec')
    mod.__file__ = url
    mod.__package__ = ''
    exec(code, mod.__dict__)
    return mod


fib = load_module('http://localhost:15000/fib.py')
print(fib)
for i in range(10):
    print(fib.fib(i), end=',')
print()

spam = load_module('http://localhost:15000/spam.py')
print(spam)
spam.hello('Guido')
