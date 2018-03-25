#!usr/bin/env python

#Yi Herng Ong Lab 7
#SID 932278854
import numpy as np
import random
import math
import matplotlib.pyplot as plt
import sys

#Approximation of definite integral using trapezoidal rule
def integrate(f,a,b,c=4):
	#Check whether the arguments are valid
	try:
		a1 = a + 1
		b1 = b + 1
		c1 = c + 1
		val = f(a)
	except TypeError:
		sys.exit('Please enter a valid function f, integer or float for interval [a,b], and integer for number of intevals')

	x1 = float(a)
	x2 = float(b)
	#Calculate delta x using number of intervals
	del_x = abs(x1-x2) / c

	arr = np.linspace(a,b,c+1)
	area = 0.0

	#Using trapezoidal rule to estimate area under function
	for idx, x in enumerate(arr):
		if x == a or x == b:
			area = area + 0.5*del_x*f(x)
		else:
			area = area + 0.5*del_x*2*f(x)

	return area

#Create mathematical function that takes one variable
def f(x):
	a = 1
	b = 2
	c = 3
	func = a*x**2 + b*x + c
	return func

#Plot absolute error in the approximation of using trapezoidal rule and Monte Carlo
#as function of number of interval and number of samples respectively
def plot_abs_error(integrate,f,xmin,xmax,actual,t=None):
	approx = 0
	abs_error = []
	#Plot as function of number of interval using trapezoid approx function
	if not t:
		num_interval = 100
		for i in xrange(num_interval):
			if i == 0: #when number of interval equal to 0, skip to the next
				pass
			else:
				approx = integrate(f,xmin,xmax,i)
				abs_error.append(abs(actual - approx))
		arr = np.arange(len(abs_error))
		plt.plot(arr, abs_error)
		plt.xlabel('Number of intervals')
		plt.ylabel('Absolute Error')
		plt.title('Trapezoidal Rule Approximation')
		plt.show()
	#PLot as function of number of samples using Monte Carlo integration
	else:
		num_samples = 1000
		for i in xrange(num_samples):
			if i == 0: #when number of samples equal to 0, skip to the next 
				pass
			else:
				approx = integrate(f,xmin,xmax,t,i)
				abs_error.append(abs(actual - approx))		
		arr = np.arange(len(abs_error))
		plt.plot(arr, abs_error)
		plt.xlabel('Number of samples')
		plt.ylabel('Absolute Error')
		plt.title('Monte Carlo Integration')
		plt.show()
	return None

#Approximation of definite integral using Monte Carlo integration
def integrate_mc(f,a,b,t,c):
	#Check whether all arguments are valid
	try:
		a1 = a + 1
		b1 = b + 1
		c1 = c + 1
		val = f(a)
		t1 = t[0] + 1
		t2 = t[1] + 1
	except TypeError:
		sys.exit('Please enter a valid function f, integer or float for interval [a,b], integer for number of samples, integer or float for elements in tuple')

	xmin = float(a)
	xmax = float(b)
	ymin = float(t[0]) 
	ymax = float(t[1])
	count = 0
	#Determine area of bounding box
	rec_area = abs(xmax - xmin) * abs(ymax - ymin)

	#Generate random points and count how many random points are in the area of function
	for i in xrange(c):
		randx = np.random.uniform(xmin, xmax)
		randy = np.random.uniform(t[0], t[1])
		if randy < f(randx) and randy > 0 and f(randx) > 0:
			count += 1
		elif randy > f(randx) and randy < 0 and f(randx) < 0:
			count -= 1
	area = rec_area * count / c
	return area

#Approximation of pi using a circle within a square box of length 2
def approximate_pi(n):
	count = 0
	xmin = -1.0
	xmax = 1.0
	ymin = -1.0
	ymax = 1.0
	sq_area = abs(xmax - xmin)*abs(ymax - ymin)

	for i in xrange(n):
		x = np.random.uniform(xmin,xmax)
		y = np.random.uniform(ymin,ymax)
		goal = x**2 + y**2
		if goal < 1:
			count += 1

	return sq_area * count / n

def generate_tuple(f,a,b):
	t = []
	t.append(f(a) - 4)
	t.append(f(b) + 4)
	return tuple(t)

if __name__ == '__main__':
	area = integrate(f,0,4,1000)
	print 'Approximation of integral using trapezoidal rule: ' + str(area)
	area_mc = integrate_mc(f,0,4,generate_tuple(f,0,4), 1000)
	print 'Approximation of integral using Monte Carlo: ' + str(area_mc)
	plot_abs_error(integrate, f, 0, 4, 49.333)
	plot_abs_error(integrate_mc, f, 0, 4, 49.333, (0,30))	
	print 'Approximation of pi using Monte Carlo sampling: ' + str(approximate_pi(1000))