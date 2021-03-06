# 执行外部命令并获取它的输出

使用 subprocess.check_output() 函数来执行外部命令，例如：
```py
import subprocess
out_bytes = subprocess.check_output(['netstat', '-a'])
```

如果需要文本形式返回，可以加一个解码步骤
```py
out_text = out_bytes.decode('utf-8')
```