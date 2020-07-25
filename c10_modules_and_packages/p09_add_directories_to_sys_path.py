""" 将文件夹加入到sys.path """


# 第一种方法，可以使用PYTHONPATH环境变量来添加
'''
$env:PYTHONPATH="D:\code\cookbook\c10_modules_and_packages\p09"
'''

# 第二种方法，可以创建一个.pth文件，将目录列举出来，再将这个.pth文件放在某个Python的site-packages目录中
'''
# myapplication.pth
D:\code\cookbook\c10_modules_and_packages\p09
'''

# 在代码中手动调节sys.path的值是不好的。
# 虽然这能“工作”，但是在实践中极为脆弱，应尽量避免使用。
# import sys
# sys.path.insert(0, 'D:\code\cookbook\c10_modules_and_packages\p09')

# 这种方法的问题是，它将目录名硬编码到了源代码中。如果代码被移到一个新的位置，这会导致维护问题。更好的做法是在不修改源代码的情况下，将path配置到其他地方。
# 如果使用模块级的变量来精心构造一个适当的绝对路径，有时可以解决硬编码目录的问题，比如__file__
import sys
from os.path import join, abspath, dirname
sys.path.insert(0, join(abspath(dirname(__file__)), 'p09'))


import spam
spam.foo()
