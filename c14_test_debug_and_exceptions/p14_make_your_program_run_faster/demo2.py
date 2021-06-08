from timeit import timeit


class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value


a = A(1, 2)

print(timeit('a.x', 'from __main__ import a'))
print(timeit('a.y', 'from __main__ import a'))
