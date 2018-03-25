#!/usr/bin/env python

from math import pi
from math import sqrt
from math import factorial

def estimate_pi():
    formula = 0.0
    sum = 0.0
    est = 0.0
    flag = 1.0
    k = 0
    while flag:
        formula = ((factorial(4.0*k))*(1103.0 + 26390.0*k)) / (((factorial(k))**4.0)*(396.0**(4.0*k)))
        sum = ((2.0*sqrt(2.0)) / 9801.0)*formula
        est = est + sum
        k += 1
        if sum < 1e-15:
            return 1/est
            break


if __name__ == '__main__':
    est_pi = estimate_pi()
    print 'The estimate of pi is' + ' ' + str(est_pi)
    print 'The math.pi is' + ' ' + str(pi)
