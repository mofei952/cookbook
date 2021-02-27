# 终止程序并给出错误信息

当想要终止某个程序时，可能会像下面这样写：

```py
import sys
sys.stderr.write('It failed!\n')
raise SystemExit(1)
```

如果直接将消息作为参数传给SystemExit()，那么可以省略import语句和将错误消息写入sys.stderr

```py
raise SystemExit('It failed')
```
