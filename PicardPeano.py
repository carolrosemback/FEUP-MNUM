from math import *


def f(x):
    return e**x - 4*(x**2)

def g(x):
    return sqrt(e**x)/2



def PicardPeano(x, it):
    for i in range(it):
        x = g(x)
        print(x)

PicardPeano(-1, 1)
