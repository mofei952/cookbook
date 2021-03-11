# 执行外部命令并获取它的输出

使用 subprocess.check_output() 函数来执行外部命令，例如：
```py
import subprocess
out_bytes = subprocess.check_output(['netstat', '-a'])
```

如果需要文本形式返回，可以加一个解码步骤，如下：
```py
out_text = out_bytes.decode('utf-8')
```

如果被执行的命令以非零码返回，就会抛出异常。下面的例子捕获到错误并获取状态码
```py
try:
    out_bytes = subprocess.check_output(['ls', '-abc'])
except subprocess.CalledProcessError as e:
    out_bytes = e.output
    code = e.returncode
```

默认情况下，check_output()仅仅返回输入到标准输出的值。如果同时需要收集标准输出和错误输出，可以使用stderr参数：
```py
out_bytes = subprocess.check_output(['pwd', '-a'], stderr=subprocess.STDOUT)
```

使用timeout参数可以增加超时机制
```py
try:
    out_bytes = subprocess.check_output(['sleep', '10'], timeout=5)
except subprocess.TimeoutExpired as e:
    out_bytes = e.output
    code = e.returncode
```

如果想让命令被一个shell执行，传递一个字符串参数，并设置参数 shell=True 。 有时候想要Python去执行一个复杂的shell命令的时候这个就很有用了，比如管道流、I/O重定向和其他特性。
```
out_bytes = subprocess.check_output('pwd | grep w', shell=True)
```

如果需要对子进程做更复杂的交互，比如给它发送输入，这时候可直接使用 subprocess.Popen 类。
```py
# Some text to send
text = b'''
hello world
this is a test
goodbye
'''

# Launch a command with pipes
p = subprocess.Popen(['wc'],
          stdout = subprocess.PIPE,
          stdin = subprocess.PIPE)

# Send the data and get the output
stdout, stderr = p.communicate(text)

# To interpret as text, decode
out = stdout.decode('utf-8')
err = stderr.decode('utf-8')
```