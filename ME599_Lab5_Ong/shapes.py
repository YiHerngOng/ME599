#!/usr/bin/env python

from math import pi
class Circle:
	def __init__(self, radius):
		self.r = radius

	def area(self):
		return pi*self.r**2

	def diameter(self):
		return 2*self.r

	def perimeter(self):
		return 2*pi*self.r

class Rectangle:
	def __init__(self,length,width):
		self.l = length
		self.w = width

	def area(self):
		return self.l*self.w

	def perimeter(self):
		return 2*(self.l + self.w)

if __name__ == '__main__':
	c = Circle(1.2)
	print 'Circle radius: ', c.r
	a = c.area()
	print 'Circle area: ', ("%0.2f" %a)
	d = c.diameter()
	print 'Circle diameter: ',d
	p = c.perimeter()
	print 'Circle perimeter: ',("%0.2f" %p)

	r = Rectangle(2,3)
	a_rec = r.area()
	print 'Rectangle area: ',("%0.2f" %a_rec)
	p_rec = r.perimeter()
	print 'Rectangle perimeter: ', ("%0.2f" %p_rec)
