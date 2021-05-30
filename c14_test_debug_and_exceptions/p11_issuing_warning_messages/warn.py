import warnings


def func(x, y, logfile=None, debug=False):
    if logfile is not None:
        warnings.warn('logfile argument deprecated', DeprecationWarning)


func(1, 2, logfile='a.txt')


# python3 example.py
# python3 -W all example.py
# python3 -W error example.py
