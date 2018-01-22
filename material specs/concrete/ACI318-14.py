#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 14:34:22 2017

@author: sean
"""

#ACI 318 design assistant
#Chap 2
#load combinations
global soilbearingpressure
soilbearingpressure = 1500

from pint import UnitRegistry
unit = UnitRegistry()

def load_combo(D=0, Lr =0, S =0, R=0,W=0,L=0,E=0,H=0):
    L1 = 1.4*D
    opt1 = [Lr,S,R]
    opt2 = [L,0.5*W]
    L2 = 1.2*D+1.6*L+.5*max(opt1)
    L3 = 1.2*D + 1.6*max(opt1) + max(opt2)
    L4 = 1.2*D + W + L + .5*max(opt1)
    L5 = 1.2*D + E + L + .2*S
    L6 = 0.9*D + W
    L7 = 0.9*D + E 
    max_load = max(L1,L2,L3,L4,L5,L6,L7)+H
    return max_load
D = 30
Dwall = 18 *unit.pound/(unit.foot**2) * 27*unit.foot 
print(Dwall)
def min_ftg(plf):
    width = plf / soilbearingpressure
    print(width)
    depth = plf / 4
    print(depth)
    return [width,depth]

def min_steel_beam(fy = 60000, fc = 3000):
    w = int(input("what is the height\n"))
    b = int(input('what is the with\n'))
    Ag = b * w
    if (( b*w) / 20) > .02:
        print("reinforcing is adequate")
    else:
        print("add more steel")
    
#D = Dwall
L = 50
print(load_combo(D,L))


#ACI SP-17(14)
#Chapter 7, pg 43
#7.3.1.1
lengthft = 1
l = lengthft * 12
h = l/24
self_weight = (thickness_in*150) /12

#chap5 one way slab