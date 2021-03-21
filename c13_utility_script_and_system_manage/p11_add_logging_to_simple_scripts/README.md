# 给简单脚本增加日志功能

打印日志的最简单方式是使用 `logging` 模块。例如：

```python
import logging

def main():
    logging.basicConig(
        filename='app.log',
        level=logging.ERROR
    )

    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')

if __name__ == '__main__':
    main()
```

修改 `basicConfig` 调用的参数，可以改变输出等级，日志格式。例如：

```python
logging.basicConfig(
     filename='app.log',
     level=logging.WARNING,
     format='%(levelname)s:%(asctime)s:%(message)s')
```

日志配置也可以使用配置文件来做，可以像下面这样修改 `basicConfig()` 调用：

```python
import logging
import logging.config

def main():
    logging.config.fileConfig('logconfig.ini')
```

创建一个下面这样的文件，名字叫 `logconfig.ini` ：

```ini
[loggers]
keys=root

[handlers]
keys=defaultHandler

[formatters]
keys=defaultFormatter

[logger_root]
level=INFO
handlers=defaultHandler
qualname=root

[handler_defaultHandler]
class=FileHandler
formatter=defaultFormatter
args=('app.log', 'a')

[formatter_defaultFormatter]
format=%(levelname)s:%(name)s:%(message)s
```

`basicConfig()` 在程序中只能被执行一次。如果稍后想改变日志配置， 就需要先获取 `root logger` ，然后直接修改它。例如：

```python
logging.getLogger().level = logging.DEBUG
```

