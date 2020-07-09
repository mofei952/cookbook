""" 拆解Python字节码 """

import dis
import opcode
import types


# dis模块可以被用来输出任何Python函数的反编译结果
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
    print('Blastoff')


dis.dis(countdown)

# 获取dis()函数解析的原始字节码
c = countdown.__code__.co_code
print(c)
print()


# 可以使用opcode模块中定义的一些常量来解析原始字节码
print(opcode.opname[c[0]])
print(opcode.opname[c[1]])
print(opcode.opname[c[2]])
print()


# 将原始字节码序列转换为opcodes和参数
def generate_opcodes(codebytes):
    extended_arg = 0
    i = 0
    n = len(codebytes)
    while i < n:
        op = codebytes[i]
        i += 1
        if op >= opcode.HAVE_ARGUMENT:
            oparg = codebytes[i] + extended_arg
            extended_arg = 0
            if op == opcode.EXTENDED_ARG:
                extended_arg = oparg * 65535
                continue
        else:
            oparg = None
        i += 1
        yield (op, oparg)


for op, oparg in generate_opcodes(countdown.__code__.co_code):
    if oparg is not None:
        print('{:15} {:20} {:5}'.format(op, opcode.opname[op], oparg))
    else:
        print('{:15} {:20}'.format(op, opcode.opname[op]))
print()


# 替换任意函数的原始字节码
def add(x, y):
    return x + y


c = add.__code__
print(c)
print(c.co_code)

newbytecode = b'xxxxxxx'
nc = types.CodeType(c.co_argcount, c.co_kwonlyargcount, c.co_nlocals,
                    c.co_stacksize, c.co_flags, newbytecode, c.co_consts,
                    c.co_names, c.co_varnames, c.co_filename, c.co_name,
                    c.co_firstlineno, c.co_lnotab)
print(nc)
add.__code__ = nc
print(add(2, 3))
