#!usr/bin/env python3
#this module is to test the function of the circle.py syscall via fabric


from math import pi
from fabric.api import local


def mult(r):

    return pi*(r**2)

radii = [12, 34, -2, "True", 32, 0, "no" ]
message = "my radius is r = {} and area is A = {}"
A = mult

for r in radii:
local("mult(r)")
    
