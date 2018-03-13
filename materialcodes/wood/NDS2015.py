#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 13:11:41 2017

@author: sean
"""
import pint
import attr

ur = pint.UnitRegistry()

@attr.s
class notation(object):
    meaning = attr.ib()
    z = 1*ur.dimensionless
    units = attr.ib(default = 1*ur.dimensionless)

import NDS2015variables as ndv
#SS 1.6

import buildingcodes.IBC as ibc

loads = ibc.Chap16()

#2.4.2
loadDurationFactor = {'':''}

#2.3.2 load duration factor
loadlong = {'permanent':{'Cd':.9,'ex':'dead load'}, #applies to ASD only!
            'ten years':{'Cd':1.0,'ex':'live load'},
            'two months':{'Cd':1.15,'ex':'snowload'}}
#2.3.2
cD = {'perm':.9,'teny':1,'twom':1.15,'sevd':1.25,'tenm':1.6,'imp':2}
phivals = {'Fb' : .85, 'Ft':.8,'Fv':.75,
           'Frt':.75,'Fs':.75,'Fc':.9,
           'Fcp':.9}
#2.3.3

#todo fill out table on pg 11 - 2.3.3

#2.3.4 Fire Retardant treatment
isfireretardanttreated  = False
temperatureFactor = 1.0 #fill out later, NDS 2.3.3

#2.3.5 Format conversion factor Kf

#use when converting factors to LRFD, i'm a little skeptical on usage

#chapter 3
#----------------
#chapter three is about analyzing bending stresses on wood

#3.1.1 scope
# scope is general design provisions for NdS, DCR < 1

#3.1.2 Net section is section
#assumed to be rectangular until #todo section design is made

#3.1.2.2 row dimensions
#rows shall be assumed to be the same if less than 4 nail diameter dif

#3.1.3 connections shall be symmetrical if able

#3.1.4 when members are more than one layer time dependance must be accounte dfor #todo joists + shtg applicable?

#3.1.5 physics applies to composits (TJI's for example -- todo pull TJI values from their listings

#3.2 span length = length + 1/2 bearing length on each end
spanlength = 10*ur.feet
spanlength = spanlength + 4*ur.inch

#3.3.1
demand, capacity = 80, 100
dcr = demand / (capacity * phivals['Fb'])

if not dcr <= 1:
    print(f'Your DCR is {dcr} please update your design.')
else:
    print(f'Your DCR is {round(dcr,2)} have a nice day.')

#3.3.2 flexural deisgn
import physics.beamdesign as demand
_, M, _= demand.simplebeamuniformload(10,10)
M = M*ur.inch*ur.lb
b = 1.5*ur.inch
d = 3.5*ur.inch

fb = (6*M)/(b*(d**2))
assert fb.dimensionality == '[mass] / [length] ** 2'

momI = (b*d**3)/12
print(momI.dimensionality)


assert momI.dimensionality == '[length] ** 4'

secmod = (b*d**2)/6
assert secmod.dimensionality == '[length] ** 3'
cL = notation('beam stability factor', 'inch')

el_e = 1

Rb = (el_e * d / (b**2))

if not Rb._magnitude<50:
    print('Rb sucks')
else:
    print('rb is cool')
Emin = 1
Fbe = 1.2*Emin / Rb.magnitude**2
Fbs = 1
if not cL ==1:
    a = (1+ Fbe/Fbs)/1.9
    b = (Fbe/Fbs)/0.95
    cL = a - (a**2-b)**.5

#3.4 beming members - shear
#3.4.1.1 DCR < 1
#3.4.1.2 testing required for strength of built up members EI TJI/glulam/open web

#3.4.2
V = 1 #load from demand value
fv = (3*V) / (2*b*d)

#3.4.3 May disregard uniform loads within depth of member
#may factor point loads by % of d away from point load

#if noteched in the tensoin face
#v'r = (2/3 * Fv * b * d) * (dn / d)**2
#if circular replace b*d w/ A

#when noted on the compression face
#v'r = (2/3) *rv * b *(d-(d-dn)/dn*e)

