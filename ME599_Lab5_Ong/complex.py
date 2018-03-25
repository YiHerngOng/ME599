#!/usr/bin/env python


class Complex:
	def __init__(self,real=0,imaginary=0):
		if real != 0:
			self.re = real
		else:
			self.re = 0
		if imaginary != 0:
			self.im = imaginary
		else:
			self.im = 0

	def __str__(self):
		if self.im < 0:
			return str(self.re) +  str(self.im) + "i"
		else:
			return str(self.re) + "+" +  str(self.im) + "i"


if __name__ == '__main__':
	a = Complex(1,2)
	b = Complex(1, -2)
	c = Complex(-1,2)
	d = Complex(2)
	e = Complex()
	print a	
	print b
	print c
	print d
	print e
	