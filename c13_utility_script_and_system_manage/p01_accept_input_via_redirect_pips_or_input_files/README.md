# 通过重定向/管道/文件接受输入


如果要让脚本接受任何用户认为最简单的输入方式。包括将命令行的输出通过管道传递给该脚本、 重定向文件到该脚本，或在命令行中传递一个文件名或文件名列表给该脚本。

可以使用Python内置的 fileinput 模块：
```py
#!/usr/bin/env python3
import fileinput

with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')
```

然后像下面这样调用它：
```sh
$ ls | ./filein.py
$ ./filein.py /etc/passwd
$ ./filein.py < /etc/passwd
```

fileinput.input() 创建并返回一个 FileInput 类的实例。该实例除了拥有一些有用的帮助方法外，它还可被当做一个上下文管理器使用。

因此，整合起来，如果我们要写一个打印多个文件输出的脚本，那么我们需要在输出中包含文件名和行号，如下所示：
```py
>>> import fileinput
>>> with fileinput.input('/etc/passwd') as f:
>>>     for line in f:
...         print(f.filename(), f.lineno(), line, end='')
...
/etc/passwd 1 xx
/etc/passwd 2 xx
/etc/passwd 3 xx
```
