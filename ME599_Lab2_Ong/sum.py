#!/usr/bin/env python

def sum_i(num):
    x = 0
    for i in num:
        x = x + i
    return x

def sum_r(num):
    if len(num) > 1:
        return num[0] + sum_r(num[1:])
    else:
        return num[0]


if __name__ == '__main__':
    num = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    total = sum_i(num)
    print 'Sum(iterative) is %d'%(total)
    total = sum_r(num)
    print 'Sum(recursive) is %d'%(total)
