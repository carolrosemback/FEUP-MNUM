#Exame de 2017:

from math import *

#Questao 2:

def f(x):
    return sqrt(1 + (2.5*e**(2.5*x))**2)

def trapezio(a,b,h):
    n = int((b-a)/h)
    tot = 0
    for i in range(1,n):
        tot += float(2*f(a + i*h))
    tot += f(a)+f(b)
    tot *= h/2
    return tot

r1 = trapezio(0.0,1.0,0.125)
r2 = trapezio(0.0,1.0,0.125/2)
r3 = trapezio(0.0,1.0,0.125/4)
print(r1,r2,r3)
    
quociente = (r2-r1)/(r3-r2)
print(quociente)

erro = (r3-r2)/3
print(erro)

def simpson(a,b,h):
    n = int((b-a)/h)
    tot = 0
    for i in range(1,n,2):
        tot += 4*f(a+i*h)
    for i in range(2, n-1, 2):
        tot += 2*f(a+ i*h)

    tot += f(a)+f(b)
    tot *= h/3
    return tot

r1 = simpson(0.0,1.0,0.125)
r2 = simpson(0.0,1.0,0.125/2)
r3 = simpson(0.0,1.0,0.125/4)
print(r1,r2,r3)
    
quociente = (r2-r1)/(r3-r2)
print(quociente)

erro = (r3-r2)/15
print(erro)

#Questao 4:

def f(t,T, C):
    return (-e**(-0.5/(T+273)))*C

def g(t,T,C):
    return 30*(e**(-0.5/(T+273)))*C - 0.5*(T-20)

def Euler(t,C,T,h, x_final):
    while(abs(x_final - t) > 0.00001):
        t,T,C = t + h, T + h*g(t,T,C), C + h*f(t, T, C)
        print("T =", T)
        print("C =", C)
    return T

T1 = Euler(0,2.5,25,0.25, 0.5)
T2 = Euler(0,2.5,25,0.25/2.0,0.5)
T3 = Euler(0,2.5,25,0.25/4.0,0.5)

quoc = (T2-T1)/(T3-T2) 
erro = T3-T2

print("quoc: ", quoc)
print ("erro: ", erro)

def rk4(xn_1,yn_1,zn_1,h):
    for i in range(2):
        xn = xn_1
        yn = yn_1
        zn = zn_1 
        xn_1 = xn + h
        delta_y1 = h * f(xn,yn,zn)
        delta_z1 = h * g(xn,yn,zn)

        delta_y2 = h * f(xn + h/2, yn+delta_y1/2, zn + delta_z1/2)
        delta_z2 = h * g(xn + h/2, yn+delta_y1/2, zn + delta_z1/2)

        delta_y3 = h * f(xn + h/2, yn+delta_y2/2, zn + delta_z2/2)
        delta_z3 = h * g(xn + h/2, yn+delta_y2/2, zn + delta_z2/2)

        delta_y4 = h * f(xn + h, yn+delta_y3, zn + delta_z3)
        delta_z4 = h * g(xn + h, yn+delta_y3, zn + delta_z3)

        yn_1 = yn +1/6*delta_y1 + 1/3*delta_y2 + 1/3*delta_y3 + 1/6*delta_y4
        zn_1 = zn +1/6*delta_z1 + 1/3*delta_z2 + 1/3*delta_z3 + 1/6*delta_z4
        
        print ("X = %.5f || Y = %.5f || Z = %.5f" %(xn_1,yn_1,zn_1)) 

    
rk4(0,2.5, 25, 0.25)

