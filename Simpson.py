import math as m 

##def f(x): 
##    return m.sin(x)/(x*x)
##
##
##def simpson(a,b,n):
##    total = 0
##    h = (abs(float(b-a)/n))
##    
##    for i in range(1,n,2):  
##        total += 4*f(a+i*h)
##        
##    for i in range(2,n-1,2):  
##        total+= 2*f(a+i*h)
##
##    total+= f(a)+f(b)   
##    total *= h/3
##    return total 
##
##s = (simpson(1,2,8))
##s1 = (simpson(1,2,16))
##s2 = (simpson(1,2,32))
##
##print((s1-s)/(s2-s1))
##print("erro: ",(s2-s1)/(15))
##


l = [1.04, 0.37, 0.38, 1.49, 1.08, 0.13, 0.64, 0.84, 0.12]
sl = [1.04, 0.38, 1.08, 0.64, 0.12]

def simpson_semf(l, h):
    s=0
    for i in range(1, len(l) -1):
        if i%2:
            s+= 4*l[i]
        else:
            s+= 2*l[i]
    return (h/3)*(l[0] + s + l[-1])


print("valor do integral: "simpson_semf(l, 0.25))
print("erro: "(simpson_semf(l, 0.25)- simpson_semf(sl, 0.5))/15)
