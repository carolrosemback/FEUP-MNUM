  from math import *


# Exercicio 2 do 2º teste de 2013

def y_1(x,y):
    return sin(2*y) + sin(2*x)


def Runge_Kutta_4(x,y,h):
    for i in range(4):
        del1 = h* y_1(x,y)
        del2 = h*y_1(x+ h/2, y+ del1/2)
        del3 = h*y_1(x+ h/2, y+ del2/2)
        del4 = h*y_1(x+ h, y+ del3)
        dely = del1/6 + del2/3 + del3/3 + del4/6
        y += dely
        x += h
        print("X = %.5f || Y = %.5f" %(x,y))

Runge_Kutta_4(1,1,0.125)


#Exercicio 6 do 2º teste de 2017

def f(x,y,z):
    return z
def g(x,y,z):
    return 2 + x**2 + x*z

def sistema_RK4_2ordem(xn_1,yn_1,zn_1,h):
    for i in range(3):
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
    

sistema_RK4_2ordem(1, 1 ,0, 0.25)     
    

#Exercico 1 do 2º teste de 2016

def f(t, c, T):
    return (-e**(-0.5/(T+273)))*c

def g(t, c, T):
    return 20*(e**(-0.5/(T+273)))*c - 0.5* (T-20)

def sistema_RK4(xn_1,yn_1, zn_1, h):
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
    

sistema_RK4(0, 1, 15, 0.25)


    
    
