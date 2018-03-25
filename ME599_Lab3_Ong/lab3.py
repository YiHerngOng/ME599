#!/usr/bin/env python

#Yi Herng Ong SID: 932278854
#ME 599 Lab 3
import matplotlib.pyplot as plt
from math import sin
from math import pi
import numpy as np
import random
from msd import *
import time

def sum_samples(s):
    size = s
    array = []
    for i in xrange(size):
        num = np.random.uniform(0,1,10)
        sum_sample = sum(num)
        array.append(sum_sample)

    return array


if __name__ == '__main__':
#   Lab direction 2
    x = np.linspace(0,4*pi,100)
    y = np.sin(x)
    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.title('A sine curve')
    plt.show()

#   Lab direction 3
    size = 10000
    list_ = sum_samples(size)
    plt.hist(list_)
    plt.title('Normal Distribution')
    plt.xlabel('Sum of ten samples')
    plt.ylabel('Frequency')
    plt.show()

#   Lab direction 4
    smd = MassSpringDamper(1.0,2.0,3.0)
    state,t = smd.simulate(0.0,1.0)
    pos = []
    for s in state:
        pos.append(s[0])

    plt.plot(t,pos)
    plt.xlabel('Time')
    plt.ylabel('Pos')
    plt.title('Displacement of mass over time')
    plt.show()

#   Lab direction 5
#   Sorted
    lengths = [1,10,100,1000,10000,100000,1000000]
    time_lengths = []
    for i in lengths:
        l = [random.randint(1,1000) for j in xrange(i)]
        start = time.time()
        l_sort = sorted(l)
        end = time.time()
        time_spent = end - start
        time_lengths.append(float(time_spent))

    plt.xlim(1,1000000)
    plt.plot(lengths,time_lengths)
    plt.xlabel('Length of list')
    plt.ylabel('Time')
    plt.title('Time taken using Sorted function')
    plt.show()

#   Lab direction 5.part II
#   Sum function
    lengths_1 = [1,10,100,1000,10000,100000,1000000]
    time_lengths_1 = []
    for k in lengths_1:
        l_1 = [random.randint(1,1000) for m in xrange(k)]
        start_1 = time.time()
        l_sum = sum(l_1)
        end_1 = time.time()
        time_spent_1 = end_1 - start_1
        time_lengths_1.append(float(time_spent_1))

    plt.plot(lengths_1,time_lengths_1)
    plt.xlabel('Length of list')
    plt.ylabel('Time')
    plt.title('Time taken using Sum function')
    plt.show()