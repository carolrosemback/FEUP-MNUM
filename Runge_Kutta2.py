from math import *

#nao sei se funciona, n tem exercicio pra testar

def z_1(z,t):
    return 2+ t**2 + t*z

def Runge_Kutta_2(z,y,t,h):
    for i in range(2):
        t,y, z = t + h, y + h*z, z + h*z_1(t +h/2, z+h/2 *z_1(t, z))
        
        print("T: ", t)
        print("Y: ", y)

Runge_Kutta_2(0,1,1,0.25)    
