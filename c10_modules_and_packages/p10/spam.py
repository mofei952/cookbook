# import_module()也可用于相对导入
import importlib
b = importlib.import_module('.grok', __package__)
print(b)
