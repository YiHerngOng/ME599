#!/usr/bin/env python

#Written by Yi Herng Ong
#ME 599 Homework 3
#Note: This code takes about 2 seconds to compute the lowest cost

import numpy as np
from random import uniform

def optimize(simulator, record_waypoints, done):
    baseline_cost = simulator.evaluate([(-10, -10), (10, 10)])

    waypoints = [(-10, -10), (0, 0), (10, 10)]
    record_waypoints(waypoints)

    best_cost = baseline_cost
    best_waypoints = waypoints[:]
    cost = 0

    arrx = np.arange(-10,11)
    arry = np.arange(-10,11)
    new_list = [(-10,-10),(0,0),(10,10)]
    new_list1 = []
    # Put this while statement in here to play nice with the grading software
    while not done():
    	#Start adding intermediate waypoints into new_list
    	i = uniform(-10,10)
    	j = uniform(-10,10)
    	new_list[1] = (i,j)
    	cost = simulator.evaluate(new_list)
    	if cost < best_cost:
    		best_cost = cost
    		best_waypoints = new_list[:]
    		print best_waypoints
    	# for i in arrx:
    	# 	for j in arry:
    	# 		#if current intermediate waypoint is in the list, jump to next iteration
    	# 		if (i,j) in new_list:
    	# 			continue
    	# 		new_list.append((i,j))
    	# 		#Sort the list after added new intermediate waypoints
    	# 		new_list = sorted(new_list)
    	# 		cost = simulator.evaluate(new_list)
    	# 		if cost < best_cost:
    	# 			best_cost = cost
    	# 		else:
    	# 			new_list.remove((i,j))
    				
    	#Add 300 more waypoints in between waypoints 
    	# for k in xrange(len(new_list)):
    	# 	if k > len(new_list) - 2:
    	# 		break
	    	x = np.linspace(new_list[0][0], new_list[1][0],500)
	    	y = np.linspace(new_list[0][1], new_list[1][1],500)

	    	x1 = np.linspace(new_list[1][0], new_list[2][0],500)
	    	y1 = np.linspace(new_list[1][1], new_list[2][1],500)

	    	for l in xrange(len(x)):
	    		new_wp = (x[l], y[l])
	    		new_list1.append(new_wp)
	    		new_wp1 = (x1[l],y1[l])
	    		new_list1.append(new_wp1)

    	best_cost = simulator.evaluate(new_list1)
    	best_waypoints = new_list1[:]
    	record_waypoints(best_waypoints)        

