def _x1(x2,x3): 
    return (7-x2-x3)/3

def _x2(x1,x3):
    return (4-x1-2*x3)/4

def _x3(x1,x2):
    return (5-2*x2)/5


def gaussJacobi(x1,x2,x3):
    x1_ant = x1
    x2_ant = x2
    x3_ant = x3
    for i in range(30):
        x1 = _x1(x2_ant,x3_ant)
        x2 = _x2(x1_ant,x3_ant)
        x3 = _x3(x1_ant,x2_ant)
        print("x1: %f\t x2: %f\t x3: %f\t" %(x1,x2,x3))
        if(abs(x1-x1_ant) < 10**(-3) and abs(x2-x2_ant) < 10**(-3)and abs(x3-x3_ant) < 10**(-3)):
            break

        x1_ant = x1
        x2_ant = x2
        x3_ant = x3

gaussJacobi(0,0,0)

def fx1(x2,x3,x4):
    return (x2 + x3 -x4 +1)/4.5
def fx2(x1,x3,x4):
    return (x1 - x3 +x4 -1)/4.5
def fx3(x1,x2,x4):
    return (x1 - 2*x2 + x4 -1)/4.5
def fx4(x1,x2,x3):
    return (-2*x1 + x2 + x3)/4.5

def Gauss_jacobi_4(x1,x2,x3,x4):
    x1_ant = x1
    x2_ant = x2
    x3_ant = x3
    x4_ant = x4
    for i in range(2):
        x1 = fx1(x2_ant, x3_ant, x4_ant)
        x2 = fx2(x1_ant, x3_ant, x4_ant)
        x3 = fx3(x1_ant, x2_ant, x4_ant)
        x4 = fx4(x1_ant, x2_ant, x3_ant)
        print("x1: %f\t x2: %f\t x3: %f\t x4: %f\t" %(x1,x2,x3,x4))

        x1_ant = x1
        x2_ant = x2
        x3_ant = x3
        x4_ant = x4

Gauss_jacobi_4(0.25,0.25,0.25,0.25)
        
    
    
