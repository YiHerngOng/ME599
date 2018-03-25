#!/usr/bin/env python

def gcd(a,b):
    flag = 1
    while flag:
        if a > b:
            c = a%b
            if c == 0:
                return b
                flag = 0
            else:
                a = b
                b = c
        else:
            c = b%a
            if c == 0:
                return a
                flag = 0
            else:
                b = a
                a = c


if __name__ == '__main__':
    g = gcd(12,30)
    print 'The grestest common divisor is %d'%(g)
