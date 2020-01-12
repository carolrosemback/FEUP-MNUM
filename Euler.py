from math import *

#Exercicio 4 de 2016

def y_1(T,C,t):
    return (-e**(-0.5/(T+273)))*C
def g_1(T,C,t):
    return 30*(e**(-0.5/(T+273)))*C - 0.5*(T -20)
    

def Euler(t,C,T,h):
    for i in range(2):
        t, T, C =t + t*h, T + h*g_1(T, C,t), C + h*y_1(T, C,t) 
        print("T: ", T)
        print("C: ", C)

Euler(0, 2.5,25.000,0.25)



###Exercicio 1 do exame e 2015

def y_1(T, Ta, t):
    return -0.25*(T- Ta)

def Euler(T, t, Ta,h):
    for i in range(2):
        t_ant = t
        t = t_ant  + t*h 
        T = T + h*y_1(T, Ta, t)
    print("T: ", T)

Euler(3, 5, 37, 0.4)


#Exercicio 1 de 2013

def z_1(t, z):
    return 0.5 + t**2 + t*z

def Euler(t, z, h, y):
    for i in range(2):
        t, y, z = t + h, y + h*z, z + h*z_1(t, z)
        print("Y: \t", y)

Euler(0, 1.0, 0.25, 0)

#Exercicio 6 do teste de 2017

def z_1(z,t,y):
    return 2 + t**2 + t*z

def Euler(z,t,y,h):
    for i in range(2):
        t,y,z = t +h, y +h*z, z + h*z_1(z,t,y)
        print("T:", t, "\nY:", y)

Euler(0, 1, 1,0.25)


#Exercicio 4 de 20

def y_1(T, Ta, t):
    return -0.25*(T- Ta)

def Euler(T, Ta, t, h):
    for i in range(2):
        t, T = t + h, T + h*y_1(T, Ta, t)
        print("\nT:", T)

Euler(10, 42, 5, 0.4)
