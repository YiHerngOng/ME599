#!/usr/bin/env python

from sensor import *
from null_filter import *


def mean_filter(data, filter_width = 0):
    newData = []
    #if no filter width is set, set default filter width as 3
    if filter_width == 0:
        for i,e in enumerate(data):
            if len(data[i:]) == 1:
                break
            elif data[i] == data[0]:
                continue
            else:
                mean = (data[i] + data[i-1] + data[i+1]) / 3
                newData.append(mean)
        return newData

    elif filter_width % 2 == 0:
        print 'Filter Width must be odd number!'
        return None

    elif filter_width < 0:
        print 'Filter Width must be positive!'
        return None

    else:
        for i,e in enumerate(data):
            sum_mean = 0
            if len(data[i:]) < filter_width:
                break
            for j in xrange(filter_width):
                sum_mean = sum_mean + data[i+j]
            mean = sum_mean / filter_width
            newData.append(mean)

        return newData

def median_filter(data,filter_width):
    newData = []
    #even filter width
    if filter_width % 2 == 0:
        for i,e in enumerate(data):
            if len(data[i:]) < filter_width:
                break
            median = (data[i + (filter_width/2) - 1] + data[i + (filter_width/2)]) / 2
            newData.append(median)

        return newData

    #Odd filter width
    else:
        for i,e in enumerate(data):
            if len(data[i:]) < filter_width:
                break
            median = data[i+(filter_width/2)]
            newData.append(median)

        return newData



if __name__ == '__main__':
        data_ = generate_sensor_data()
        print_sensor_data(data_,'raw_b4_mean')

        #Apply mean filter
        filtered_data = mean_filter(data_)
        print_sensor_data(filtered_data,'mean_data')
        filtered_data_1 = mean_filter(data_,9)
        if filtered_data_1:
            print_sensor_data(filtered_data_1,'var_width_mean_data')

        #Apply Median filter
        filtered_data_2 = median_filter(data_, 6)
        print_sensor_data(filtered_data_2,'median_data')

