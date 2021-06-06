import time


time.sleep(10)

n = 0
for i in range(10000):
    n += 1


"""
$ time python demo.py

real    0m11.525s
user    0m0.219s
sys     0m1.328s

$ python -m cProfile demo.py
         4 function calls in 10.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001   10.002   10.002 demo.py:1(<module>)
        1    0.000    0.000   10.002   10.002 {built-in method builtins.exec}
        1   10.000   10.000   10.000   10.000 {built-in method time.sleep}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""