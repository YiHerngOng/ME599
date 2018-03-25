import math


def cylinder_volume(r,h):
    #check if both arguments are positive
    if r > 0 and h > 0:
        return (math.pi*r**2)*h
    else:
        return "None"

def torus_volume(outer_rad,inner_rad):
    #check if both arguments are positive
    if inner_rad < 0 or outer_rad < 0:
        return "None"
    else:
        rad = (outer_rad - inner_rad)/2.0
        #check if inner rad is smaller than outer radq
        if rad < 0.0:
            return "None"
        else:
            r1 = inner_rad + rad
            vol = (math.pi*(rad**2)) * (2*math.pi*r1)
            return vol

if __name__ == '__main__':
    #calculate volume of cylinder
    r = 3
    h = 5
    print cylinder_volume(r,h)
    #calculate volume of torus
    inner_rad = 3
    outer_rad = 4
    print torus_volume(outer_rad,inner_rad)



