# 创建和解压归档文件

创建或解压常见格式的归档文件（比如.tar, .tgz或.zip）可以使用 shutil 模块的 make_archive() 函数和 unpack_archive() 函数。例如：

```py
>>> import shutil
>>> shutil.unpack_archive('Python-3.3.0.tgz')

>>> shutil.make_archive('py33','zip','Python-3.3.0')
'/Users/beazley/Downloads/py33.zip'
>>>
```

make_archive() 的第二个参数是期望的输出格式。 可以使用 get_archive_formats() 获取所有支持的归档格式列表。例如：

```py
>>> shutil.get_archive_formats()
[('bztar', "bzip2'ed tar-file"), ('gztar', "gzip'ed tar-file"), ('tar', 'uncompressed tar file'), ('xztar', "xz'ed tar-file"), ('zip', 'ZIP file')]
>>>
```

