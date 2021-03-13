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

如果源文件是一个符号链接，那么目标文件将会是符号链接指向的文件。如果想复制符号链接本身，那么需要指定关键字参数 follow_symlinks ，如下：

```py
shutil.copytree(src, dst, symlinks=True)
```

copytree() 可以在复制过程中选择性的忽略某些文件或目录，可以指定一个忽略函数来实现：

```py
def ignore_pyc_files(dirname, filenames):
    return [name in filenames if name.endswith('pyc')]

shutil.copytree(src, dst, ignore=ignore_pyc_files)
```

忽略某种模式的文件名是很常见的，因此一个便捷的函数 ignore_patterns() 已经包含在里面了。例如：
```py
shutil.copytree(src, dst, ignore=shutil.ignore_patterns('*~', '*.pyc'))
```