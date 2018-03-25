#!/usr/bin/env python
#Yi Herng Ong Lab8
#SID 932278854
import numpy as np
import random as rd
import matplotlib.pyplot as plt
from scipy import optimize
from math import sqrt

def optimize_step(f, bounds, n):
	arr = np.linspace(bounds[0], bounds[1], n)
	max_x = 0
	yarr = []
	for idx, x in enumerate(arr):
		if idx == 0:
			pass
		elif f(arr[idx-1]) < f(arr[idx]):
			max_x = x
	return max_x

def optimize_random(f,bounds,n):
	arr = np.random.uniform(min(bounds),max(bounds),n)
	#print arr
	max_x = 0
	yarr = []
	for idx, x in enumerate(arr):
		yarr.append(f(x))

	for idy, y in enumerate(yarr):
		if y == max(yarr):
			max_x = arr[idy]

	return max_x

def optimize_gradient(f, bounds, epsilon):
	step_size = abs(bounds[1] - bounds[0]) / 1000
	x_1 = rd.uniform(bounds[0],bounds[1])
	x_0 = bounds[0]
	while True:
		if abs(x_1 - x_0) == 0.0:
			break
		grad = (f(x_1) - f(x_0)) / (x_1 - x_0)
		if abs(step_size*grad) < epsilon:
			break
		x_0 = x_1 
		x_1 = x_0 + (step_size*grad)
	return x_1

def scipy_approach(f, bounds=None):
    return optimize.minimize_scalar(lambda x: -f(x), None)

def f(x,y=0):
	a = 1
	b = 2
	c = 1
	if y==0:	
		return -a*x**2 + b*x + c
	else:
		return -(x-2)**2 - (y-2)**2 - 10

def plot_performance(f, bounds):
	n = range(1001)
	diff = []
	diff1 = []
	diff2 = []
	diff3 = []
	actual_x = 1.0

	#Evaluate difference between calculated x in each optimize fucntions and actual x
	for i in n[1:]:
		max_x = optimize_step(f,bounds,i)
		diff.append(abs(max_x - actual_x))
		max_x1 = optimize_random(f,bounds,i)
		diff1.append(abs(max_x1 - actual_x))
		max_x3 = scipy_approach(f)
		diff3.append(abs(max_x3.x - actual_x))

	epsilon = [x*(10**-5) for x in n]
	epsilon = epsilon[::-1]
	for j in epsilon:
		max_x2 = optimize_gradient(f,bounds,j)
		diff2.append(abs(max_x2 - actual_x))

	arr = np.arange(len(diff))
	arr1 = np.arange(len(diff2))

	#Plot optimize step
	plt.plot(arr, diff)
	plt.xlabel('Number of intervals')
	plt.ylabel('Difference between evaluated x and actual x')
	plt.title('Performance of optimize_step')
	plt.show()

	#Plot optimize random
	plt.plot(arr, diff1)
	plt.xlabel('Number of intervals')
	plt.ylabel('Difference between evaluated x and actual x')
	plt.title('Performance of optimize_random')
	plt.show()

	#Plot optimize gradient
	plt.plot(arr1, diff2)
	plt.xlabel('Number of intervals')
	plt.ylabel('Difference between evaluated x and actual x')
	plt.title('Performance of optimize_gradient')
	plt.show()

	#Plot scipy approach
	plt.plot(arr, diff3)
	plt.xlabel('Number of intervals')
	plt.ylabel('Difference between evaluated x and actual x')
	plt.title('Performance of scipy_approach')
	plt.show()
	return None


def optimize_md(f,bounds):
	x0 = []
	#Set initial values x0
	for i in bounds:
		x0.append(i[0])
	#Evaluate maximum using optimize.minimize
	res = optimize.minimize(lambda var:-f(var[0],var[1]),x0,bounds = bounds)
	return tuple(res.x)


if __name__ == '__main__':
	print 'Optimize step function:', optimize_step(f,(0.0,4.0),1000)
	print 'Optimize random: ', optimize_random(f, (0.0,4.0),1000)
	print 'Optimize gradient: ', optimize_gradient(f, (0.0,4.0), 0.000005)
	res = optimize_md(f,[(-10, 10), (-10, 10)])
	print 'Optimize multidimensional: ', res
	plot_performance(f,(0.0,4.0))
