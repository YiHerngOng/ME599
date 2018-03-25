#!/usr/bin/env python
#ME 599 Lab 6
#Yi Herng Ong SID 932278854

class Complex:
	def __init__(self,real=0,imaginary=0):
		self.re = float(real)
		self.im = float(imaginary)


	def __str__(self):
		return '({0} {1} {2}i)'.format(self.re, '-' if self.im < 0 else '+', abs(self.im))

	def __add__(self,other):
		a = Complex()
		try:
#			return '{0} {1} {2}i'.format((self.re + other.re), '-' if (self.im + other.im) < 0 else '+', abs(self.im + other.im))
			a = Complex()
			a.re = self.re + other.re
			a.im = self.im + other.im
			return a
		except:
			a.re = self.re + other
			a.im = self.im 
			return a	

	def __radd__(self,other):
		return self.__add__(other)

	def __sub__(self,other):
		return self + (-other)

	def __rsub__(self,other):
		return self.__add__(-other)

	def __neg__(self):
		a = Complex()
		a.re = -self.re
		a.im = -self.im
		return a

	def __mul__(self,other):
		a = Complex()
		try:
#			return '{0} {1} {2}i'.format(((self.re * other.re) - (self.im * other.im)), '-' if ((self.re * other.im) + (self.im * other.re)) < 0 else '+', abs((self.re * other.im) + (self.im * other.re)))
			a.re = self.re * other.re - self.im * other.im
			a.im = self.re * other.im + self.im * other.re
			return a		
		except:
#			return '{0} {1} {2}i'.format((self.re * other), '-' if (self.im * other) < 0 else '+', abs(self.im * other))
			a.re = self.re * float(other)
			a.im = self.im * float(other)
			return a

	def __rmul__(self,other):
		return self.__mul__(other)


	def __div__(self,other):
		a = Complex()
		try:
#			return '{0} {1} {2}i'.format(((self.re * other.re) - (self.im * other.im)), '-' if ((self.re * other.im) + (self.im * other.re)) < 0 else '+', abs((self.re * other.im) + (self.im * other.re)))
			a.re = (self * ~other).re / (other.re**2 + other.im**2)
			a.im = (self * ~other).im / (other.re**2 + other.im**2)
			return a
		except:
			a.re = self.re / other
			a.im = self.im / other
			return a

	def __rdiv__(self,other):
		a = Complex()
		a.re = (~self * other).re / (self.re**2 + self.im**2)
		a.im = (~self * other).im / (self.re**2 + self.im**2)
		return a


	def __invert__(self):
		a = Complex()
		a.re = self.re
		a.im = -self.im
		return a

	def __repr__(self):
		return self.__str__()

if __name__ == '__main__':
	a = Complex(1,2)
	b = Complex(3,4)
	c = (a+b, a-b)
	d = (a,b)

	print 'Addition:'
	print a + b
	print a + 1.0
	print 1.0 + a

	print 'Subtraction:'
	print a - b
	print a - 2.0
	print 2.0 - a

	print 'Multiplication:'
	print a * b
	print a * 2.0
	print 2.0 * a

	print 'Division:'
	print a / b
	print a / 2.0
	print 1.0 / a

	print 'Conjugate:{0}, Negation:{1}'.format(~a, -a)

	print c
	print d
	