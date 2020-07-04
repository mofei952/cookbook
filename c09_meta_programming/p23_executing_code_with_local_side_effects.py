""" 在局部变量域中执行代码 """


# 在一个函数中执行exec，不能直接取到修改过后的变量值
def test1():
    a = 13
    exec('b = a + 1')
    print(b)


# test1()  # NameError: name 'b' is not defined


# 在调用exec()之前使用locals函数来得到一个局部变量字典，
# 之后就能从这个字典中取到修改过后的变量值了
def test2():
    a = 13
    loc = locals()
    print(loc)
    exec('b = a + 1')
    print(loc)
    print(loc['b'])


test2()
print()


# 要注意的是每次locals()被调用的时候，它会获取局部变量的值并覆盖字典中相应的变量
def test3():
    a = 13
    loc = locals()
    print(loc)
    exec('a = a + 1')
    print(loc)
    locals()
    print(loc)


test3()
print()


# 作为locals()的一个替代方案，可以使用自己的字典，并将它传递给exec()
def test4():
    a = 13
    loc = {'a': a}
    glb = {}
    exec('b = a + 1', glb, loc)
    b = loc['b']
    print(b)


test4()
