""" 读取位于包中的数据文件 """

# 在包中使用pkgutil.get_data()来读取数据文件
from p08.spam import data
print(data)
