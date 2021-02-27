# 解析命令行选项

为了解析命令行选项，你首先要创建一个 ArgumentParser 实例， 并使用 add_argument() 方法声明你想要支持的选项。

在每个 add_argument() 调用中，dest 参数指定解析结果被指派给属性的名字。 metavar 参数被用来生成帮助信息。

action 参数指定跟属性对应的处理逻辑， 通常的值为 store ,被用来存储某个值或将多个参数值收集到一个列表中。

下面的参数收集所有剩余的命令行参数到一个列表中。在本例中它被用来构造一个文件名列表：
```
parser.add_argument(dest='filenames',metavar='filename', nargs='*')
```

下面的参数根据参数是否存在来设置一个 Boolean 标志：
```
parser.add_argument('-v', dest='verbose', action='store_true',
                    help='verbose mode')
```

下面的参数接受一个单独值并将其存储为一个字符串：
```
parser.add_argument('-o', dest='outfile', action='store',
                    help='output file')
```

面的参数说明允许某个参数重复出现多次，并将它们追加到一个列表中去。 required 标志表示该参数至少要有一个。-p 和 --pat 表示两个参数名形式都可使用。
```
parser.add_argument('-p', '--pat',metavar='pattern', required=True,
                    dest='patterns', action='append',
                    help='text pattern to search for')
```

下面的参数说明接受一个值，但是会将其和可能的选择值做比较，以检测其合法性：
```
parser.add_argument('--speed', dest='speed', action='store',
                    choices={'slow','fast'}, default='slow',
                    help='search speed')
```

一旦参数选项被指定，你就可以执行 parser.parse() 方法了。 它会处理 sys.argv 的值并返回一个结果实例。 每个参数值会被设置成该实例中 add_argument() 方法的 dest 参数指定的属性值。
