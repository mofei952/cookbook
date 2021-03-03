# 获取终端的大小

使用 os.get_terminal_size() 函数可以得到当前终端的大小。

代码示例：
```python
>>> import os
>>> sz = os.get_terminal_size()
>>> sz
os.terminal_size(columns=80, lines=24)
>>> sz.columns
80
>>> sz.lines
24
>>>
```
