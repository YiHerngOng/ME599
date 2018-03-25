#!/usr/bin/env python
#ME 599 Lab6
#Yi Herng Ong SID 932278854

from math import sqrt

class Roots:
	def __init__(self,a=1,b=0,c=0):
		if a == 0:
			raise ValueError
		self.a = float(a)
		self.b = float(b)
		self.c = float(c)


	def __str__(self):
		discriminant  = self.b**2 - (4*self.a*self.c)
		if discriminant == 0:
			return '({0})'.format(self.b / (2*self.a))
		elif discriminant > 0:
			r1 = (-self.b + sqrt(discriminant)) / (2*self.a)
			r2 = (-self.b - sqrt(discriminant)) / (2*self.a)
			return '({0}, {1})'.format(r1,r2)
		else:
			r1re = -self.b / (2*self.a)
			r1im = sqrt(discriminant*-1) / (2*self.a)
			return '({0}, {1})'.format(("%.2f" % r1re) + '+' + ("%.3f" % r1im) + 'i', ("%.2f" % r1re) + '-' + ("%.3f" % r1im) + 'i')




if __name__ == '__main__':
	r = Roots(5,12,90)
	print r
