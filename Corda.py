import math as m

def f(x):
    return x - 2 * m.log(x) - 5


def Corda(a, b):
    for i in range(3):
        w = (a*f(b) - b*(f(a)))/(f(b)-f(a))
        if (f(a)*f(w) < 0):
            b = w
        else:
            a = w
        print("A: ",a)
        print("B: ",b)
        print('f(a): {0:.10f}\t f(b): {1:.10f}\t x: {2:.10f}\t '.format(f(a), f(b), w))


Corda(0.01, 1)
