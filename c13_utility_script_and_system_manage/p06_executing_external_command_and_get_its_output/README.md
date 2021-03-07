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
