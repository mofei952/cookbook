# 复制或者移动文件和目录

shutil 模块有很多便捷的函数可以复制文件和目录。比如：

```py
import shutil

# Copy src to dst. (cp src dst)
shutil.copy(src, dst)

# Copy files, but preserve metadata (cp -p src dst)
shutil.copy2(src, dst)

# Copy directory tree (cp -R src dst)
shutil.copytree(src, dst)

# Move src to dst (mv src dst)
shutil.move(src, dst)
```

这些函数的参数都是字符串形式的文件名或目录名。底层语义模拟了类似的Unix命令，如上面的注释部分。

如果源文件是一个符号链接，那么目标文件将会是符号链接指向的文件。如果想复制符号链接本身，那么需要指定关键字参数 symlinks ，如下：

```py
shutil.copytree(src, dst, symlinks=True)
```

copytree() 可以在复制过程中选择性的忽略某些文件或目录，可以指定一个忽略函数来实现：

```py
def ignore_pyc_files(dirname, filenames):
    return [name for name in filenames if name.endswith('pyc')]

shutil.copytree(src, dst, ignore=ignore_pyc_files)
```

忽略某种模式的文件名是很常见的，因此一个便捷的函数 ignore_patterns() 已经包含在里面了。例如：

```py
shutil.copytree(src, dst, ignore=shutil.ignore_patterns('*~', '*.pyc'))
```

对于文件元数据信息，copy2() 这样的函数只能尽自己最大能力来保留它。 访问时间、创建时间和权限这些基本信息会被保留， 但是对于所有者、ACLs、资源fork和其他更深层次的文件元信息就说不准了， 这个还得依赖于底层操作系统类型和用户所拥有的访问权限。 所以通常不会去使用 shutil.copytree() 函数来执行系统备份。

当处理文件名的时候，最好使用 os.path 中的函数来确保最大的可移植性（特别是同时要适用于Unix和Windows）。 例如：

```py
>>> filename = '/Users/guido/programs/spam.py'
>>> import os.path
>>> os.path.basename(filename)
'spam.py'
>>> os.path.dirname(filename)
'/Users/guido/programs'
>>> os.path.split(filename)
('/Users/guido/programs', 'spam.py')
>>> os.path.join('/new/dir', os.path.basename(filename))
'/new/dir/spam.py'
>>> os.path.expanduser('~/guido/programs/spam.py')
'/Users/guido/programs/spam.py'
>>>
```

在复制过程中，函数可能会碰到损坏的符号链接，因为权限无法访问文件的问题等等。 为了解决这个问题，所有碰到的问题会被收集到一个列表中并打包为一个单独的异常，到了最后再抛出。


```py
try:
    shutil.copytree(src, dst)
except shutil.Error as e:
    for src, dst, msg in e.args[0]:
         # src is source name
         # dst is destination name
         # msg is error message from exception
         print(dst, src, msg)
```

如果提供关键字参数 ignore_dangling_symlinks=True ， 这时候 copytree() 会忽略掉无效符号链接。

```py
shutil.copytree(src, dst, ignore_dangling_symlinks=True)
```
