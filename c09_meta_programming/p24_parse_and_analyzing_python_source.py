""" 解析与分析Python源码 """

import ast

# Python能够计算或执行字符串形式的源代码
x = 42
eval('2 + 3 * 4 + x')
exec('for i in range(10): print(i)')
print()

# ast模块能被用来将Python源码编译成一个可被分析的抽象语法树（AST）
ex = ast.parse('2 + 3 * 4 + x', mode='eval')
print(ex)
print(ast.dump(ex))
top = ast.parse('for i in range(10): print(i)', mode='exec')
print(top)
print(ast.dump(top))
print()


# 分析AST节点最简单的方法就是定义一个访问者类，实现很多visit_NodeName()方法。
# 下面是这样一个类，记录了哪些名字被加载、存储和删除的信息
class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loaded = set()
        self.stored = set()
        self.deleted = set()

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.loaded.add(node.id)
        elif isinstance(node.ctx, ast.Store):
            self.stored.add(node.id)
        elif isinstance(node.ctx, ast.Del):
            self.deleted.add(node.id)


code = '''
for i in range(10):
    print(i)
del i
'''

top = ast.parse(code, mode='exec')
c = CodeAnalyzer()
c.visit(top)
print('Loaded:', c.loaded)
print('Stored:', c.stored)
print('Deleted:', c.deleted)

# AST可以通过compile()函数来编译并执行
exec(compile(top, '<stdin>', 'exec'))
