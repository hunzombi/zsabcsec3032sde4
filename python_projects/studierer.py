
from cmath import nan


def fib(n, m = {}):
    if n < 0:
        return nan
    if n in m.keys():
        return m[n]
    res = 0
    if n == 0:
        res = 0
    elif n < 2:
        res = 1
    else:
        res = fib(n-1, m) + fib(n-2, m)
    m[n] = res
    print(m)
    return res

r = fib(50)

print(r)