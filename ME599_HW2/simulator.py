#!/usr/bin/env python

import os
import sys
import subprocess
import random

class Simulator:
	def __init__(self, p_num):
		self.p_num = p_num


	def evaluate(self,w):
		filename = 'waypoints'
		with open(filename,'w') as f:
			for i in w:				
				f.write(str(i[0]))
				f.write(' ')
				f.write(str(i[1]))
				f.write(' ')
		output = subprocess.check_output(['simulator.exe', filename, str(self.p_num)])
		f_output = output.split()
		return float(f_output[-1][:-1])

if __name__ == '__main__':
	w = [(-10, -10), (10, 10)]
	s = Simulator(10)
	print 'Basic Waypoints: ', str(s.evaluate(w))

	filename = 'better_waypoints'
	swp = (-10,-10)
	ewp = (10,10)
	bwp = [swp, ewp]
	bwp_cost = 0
	iteration = 10
	for i in xrange(iteration):
		wp1 = random.randint(-10,10)
		wp2 = random.randint(-10,10)
		new_wp = [swp, (wp1, wp2), ewp]
		if s.evaluate(new_wp) < s.evaluate(bwp):
			bwp = new_wp
			bwp_cost = s.evaluate(bwp)

	with open(filename, 'w') as f:
		for i in bwp:				
			f.write(str(i[0]))
			f.write(' ')
			f.write(str(i[1]))
			f.write(' ')	
	print 'Better Waypoints: ', str(bwp), ' Path Cost: ', str(bwp_cost)
