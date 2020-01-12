def _x1(x2,x3,x4): 
    return (25 -0.5*x2 -3*x3 -0.25*x4)/6

def _x2(x1,x3,x4):
    return (10 - 1.2*x1 -0.25*x3 -0.2*x4)/3

def _x3(x1,x2,x4):
    return (7 + x1 -0.25*x2 -2*x4)/4

def _x4(x1,x2,x3):
    return (-12 -2*x1 -4*x2 -x3)/8

def gauss_Seidel(x1,x2,x3,x4):
    x1_ant = x1
    x2_ant = x2
    x3_ant = x3
    x4_ant = x4
    for i in range(30):
        x1 = _x1(x2,x3,x4)
        x2 = _x2(x1,x3,x4)
        x3 = _x3(x1,x2,x4)
        x4 = _x4(x1,x2,x3)
        print("x1: %f\t x2: %f\t x3: %f\t x4: %f\t" %(x1,x2,x3,x4))
        if(abs(x1-x1_ant) < 10**(-3) and abs(x2-x2_ant) < 10**(-3)and abs(x3-x3_ant) < 10**(-3), abs(x4-x4_ant) < 10**(-3)):
            break

        x1_ant = x1
        x2_ant = x2
        x3_ant = x3
        x4_ant = x4

gauss_Seidel(2.12687, 2.39858, 3.99517, -3.73040)
