import math as m


def f(x):
    return x**3 + 2*(x**2) + 10*x -17

def df(x):
    return 3*(x**2) + 4*x +10


def Newton(x, it):
    for i in range(it):
        x = x -f(x)/df(x)
        print(x)

Newton(0, 3)
