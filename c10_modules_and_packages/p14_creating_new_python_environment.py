""" 创建新的Python环境 """


# 可以使用pyvenv命令创建一个新的“虚拟”环境
"""
pyvenv Spam
"""

# 传给pyvenv命令的名字是将要被创建的目录名
"""
bash % cd Spam
bash % ls
bin include lib pyvenv.cfg
bash %
"""

# 在bin目录中，可以找到一个可以使用的Python解释器
"""
bash % Spam/bin/python3
Python 3.3.0 (default, Oct 6 2012, 15:45:22)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from pprint import pprint
>>> import sys
>>> pprint(sys.path)
['',
'/usr/local/lib/python33.zip',
'/usr/local/lib/python3.3',
'/usr/local/lib/python3.3/plat-darwin',
'/usr/local/lib/python3.3/lib-dynload',
'/Users/beazley/Spam/lib/python3.3/site-packages']
>>>
"""

# 这个解释器的特点就是他的site-packages目录被设置为新创建的环境。
# 如果要安装第三方包，它们会被安装在那里，而不是通常系统的site-packages目录。


# 激活虚拟环境
"""
source Spam/bin/activate
"""


# 默认情况下，虚拟环境是空的，不包含任何额外的第三方库。
# 如果想将一个已经安装的包作为虚拟环境的一部分，可以使用“–system-site-packages”选项来创建虚拟环境
"""
bash % pyvenv --system-site-packages Spam
"""
