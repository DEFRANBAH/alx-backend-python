#!/usr/bin/python3

from math import pi

def mult(r):
    if type r not in [int, float]:
        raise TypeError("no negative radius")
    if r <  0:
        raise TypeError("the radius must be a non neg number")
    return pi*(r**2)

message = "the area is {area} aof radius {radius}"
radii = [12, 4, 9, 2, 3, 0, -2, True, 2+5j, "nmany"]

for i in radii:
    A = mult(i)
    print(message.format(area=A, radius=i))

