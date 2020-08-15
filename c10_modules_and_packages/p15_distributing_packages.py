""" 分发包 """


# 编写setup.py

# 创建一个MANIFEST.in文件，列出所有在包中需要包含进来的非源码文件

# 创建一个源码分发包
"""
% bash python3 setup.py sdist
"""

# 它会创建一个文件比如”projectname-1.0.zip” 或 “projectname-1.0.tar.gz”, 具体依赖于系统平台。
# 如果一切正常， 这个文件就可以发送给别人使用或者上传至 Python Package Index.

# 拿到这个文件后解压然后执行以下命令来安装
"""
% bash python3 setup.py install
"""
