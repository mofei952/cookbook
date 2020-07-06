""" 解析与分析Python源码 """

import inspect
import ast

# Python能够计算或执行字符串形式的源代码
x = 42
print(eval('2 + 3 * 4 + x'))
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


# 分析AST节点最简单的方法就是定义一个访问者类，实现很多visit_NodeName()方法
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
print()

# AST可以通过compile()函数来编译并执行
exec(compile(top, '<stdin>', 'exec'))
print()


# 重写AST并重新创建函数代码对象来将全局访问变量降为函数体作用范围
class NameLower(ast.NodeVisitor):
    """
        Node visitor that lowers globally accessed names into
        the function body as local variables.
    """

    def __init__(self, lowered_names):
        self.lowered_names = lowered_names

    def visit_FunctionDef(self, node):
        # Compile some assignments to lower the constants
        code = '__globals = globals()\n'
        code += '\n'.join("{0} = __globals['{0}']".format(name)
                          for name in self.lowered_names)
        code_ast = ast.parse(code, mode='exec')

        # Inject new statements into the function body
        node.body[:0] = code_ast.body

        # Save the function object
        # self.func = node


# Decorator that turns global names into locals
def lower_names(*namelist):
    def lower(func):
        srclines = inspect.getsource(func).splitlines()
        # Skip source lines prior to the @lower_names decorator
        for n, line in enumerate(srclines):
            if '@lower_names' in line:
                break

        src = '\n'.join(srclines[n+1:])
        # Hack to deal with indented code
        if src.startswith((' ', '\t')):
            src = 'if 1:\n' + src
        top = ast.parse(src, mode='exec')

        # Transform the AST
        cl = NameLower(namelist)
        cl.visit(top)

        # Execute the modified AST
        temp = {}
        exec(compile(top, '', 'exec'), temp, temp)

        # Pull out the modified code object
        func.__code__ = temp[func.__name__].__code__
        return func
    return lower


INCR = 1


@lower_names('INCR')
def countdown(n):
    while n > 0:
        n -= INCR
        print(n)


countdown(10)
