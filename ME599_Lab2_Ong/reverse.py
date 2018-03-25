#!/usr/bin/env python

def reverse_i(list_):
    a = []
    for i,c in enumerate(list_):
        a.append(list_[-i-1])
    return a

def reverse_r(list_):
    if len(list_) == 1:
        return [list_[0]]
    else:
        return  reverse_r(list_[1:]) + [list_[0]]


if __name__ == '__main__':
    list_ = [2,3,4,5,6,7,8,9,13,14,15,16]
    a = reverse_i(list_)
    print 'Iterative reverse' + '=' + str(a)
    b = reverse_r(list_)
    print 'Recursive reverse' + '=' + str(b)
