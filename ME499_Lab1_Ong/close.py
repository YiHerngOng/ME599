import math

def close(a,b,c):
    diff = abs(a-b)
    if diff < c:
        print "True"
    else:
        print "False"

if __name__ == '__main__':
    close(1,2,0.5)
    close(1,2,3)
