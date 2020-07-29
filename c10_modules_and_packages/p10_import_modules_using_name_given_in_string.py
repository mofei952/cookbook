""" 通过字符串名导入模块 """

# 使用importlib.import_module()函数来手动导入名字为字符串给出的一个模块或者包的一部分
import importlib
math = importlib.import_module('math')
print(math.sin(2))

mod = importlib.import_module('urllib.request')
u = mod.urlopen('http://www.python.org')

# import_module()也可用于相对导入
from p10 import spam
