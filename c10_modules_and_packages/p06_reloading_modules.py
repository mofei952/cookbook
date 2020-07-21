""" 重新加载模块 """

# 使用imp.reload()来重新加载先前加载的模块

# 启动交互式会话
"""
>>> import spam
>>> from spam import grok
>>> spam.bar()
bar
>>> grok()
grok
>>>
"""

# 不退出Python修改spam.py的源码，将grok()修改成以下这样
"""
def grok():
    print('new grok')
"""

# 回到交互式会话，重新加载模块后，再调用函数测试
"""
>>> import imp
>>> imp.reload(spam)
<module 'spam' from 'D:\\code\\cookbook\\c10_modules_and_packages\\p06\\spam.py'>
>>> spam.bar()
bar
>>> grok()     
grok
>>> spam.grok() 
new grok
>>>
"""

# 可以看到有两个版本的grok()函数被加载。通常来说，这不是想要的。
# 因此，在生产环境中可能需要避免重新加载模块
