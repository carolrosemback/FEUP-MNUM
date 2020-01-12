import math


def f(x):
    return x**3 - 10*math.sin(x) +2.8
    



def bissection(f, a, b, numIt):
    i =0
    if(f(a)*f(b) < 0):
        while(i<numIt):
            x = (a+b)/2
            print("Root: ", x)
            if f(a)*f(x) < 0:
                b=x
                
            else:
                 a=x
            x= (a+b)/2
            print(i)
            i+= 1
            
            print("A: ",a)
            print("B: ",b)
        print("Root: ", x)
        print(f(x))
    else:
        print("No roots in given interval")


def bissection2(a,b):
	for i in range(3):
		root = (a+b)/2
		
		print("A : ",a)
		print("B : ",b)
		print('f(a):', f(a), '\tf(b):', f(b), '\tf(root):',f(root))
		
		if f(a)*f(root) < 0: 
			b = root
		else:
			a = root

		print("Root : ",root)
		print("\n")



bissection2(1.5, 4.2)


