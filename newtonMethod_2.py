import math as m

def f1(x,y):
	return x**2 - y - 1.2
def f2 (x,y):
	return y**2 -x -0.5
def df1x (x,y):
	return  2*x
def df1y (x,y):
	return -1
def df2x (x,y):
	return -1
def df2y (x,y): 
	return 2*y 


def NewtonMethod(x,y):
	for i in range(3):
		jacobian = (df1x(x,y)*df2y(x,y)) - (df1y(x,y)*df2x(x,y))
		xn = x - (f1(x,y)*df2y(x,y) - f2(x,y)*df1y(x,y))/jacobian
		yn = y - (f2(x,y)*df1x(x,y) - f1(x,y)*df2x(x,y))/jacobian
		x = xn 
		y = yn 
		print('n: {2}\t x: {0:.10f}\t y: {1:.10f}'.format(x,y,i))


NewtonMethod(1.1, 1.1)
