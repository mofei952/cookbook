""" 拆解Python字节码 """

import dis
import opcode


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
            oparg = codebytes[i] + codebytes[i+1] * 256 + extended_arg
            extended_arg = 0
            i += 2
            if op == opcode.EXTENDED_ARG:
                extended_arg = oparg * 65535
                continue
        else:
            oparg = None
        yield (op, oparg)


for op, oparg in generate_opcodes(countdown.__code__.co_code):
    print(op, opcode.opname[op], oparg)
