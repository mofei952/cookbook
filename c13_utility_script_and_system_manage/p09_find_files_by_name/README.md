# 通过文件名查找文件

查找文件可以使用 `os.walk()` 函数。下面的例子查找特定的文件名并打印文件全路径：

```python
import os

def findfile(start, name):
	for relpath, dirs, files in os.walk(start):
		if name in files:
			full_path = os.path.join(start, relpath, name)
			print(os.path.normpath(os.path.abspath(full_path)))

if __name__ == '__main__':
	findfile(sys.argv[1], sys.argv[2])
```

为了避免奇怪的路径名比如 `././foo//bar` ，使用了另外两个函数来修正结果。 第一个是 `os.path.abspath()` ,它接受一个路径，可能是相对路径，最后返回绝对路径。 第二个是 `os.path.normpath()` ，用来返回正常路径，可以解决双斜杆、对目录的多重引用的问题等。

尽管这个脚本相对于UNIX平台上面的很多查找来讲要简单很多，它还有跨平台的优势。 并且，还能很轻松的加入其他的功能。比如下面的函数打印所有最近被修改过的文件：

```python
import os
import time

def modified_within(top, seconds):
    now = time.time()
    for path, dirs, files in os.walk(top):
        for name in files:
            fullpath = os.path.join(path, name)
            if os.path.exists(fullpath):
                mtime = os.path.getmtime(fullpath)
                if mtime > (now - seconds):
                    print(fullpath)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print('Usage: {} dir seconds'.format(sys.argv[0]))
        raise SystemExit(1)

    modified_within(sys.argv[1], float(sys.argv[2]))
```

