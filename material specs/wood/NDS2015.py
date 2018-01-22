#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 13:11:41 2017

@author: sean
"""
import pint
import NDS2015variables as ndv

print("hello world")
def bending_moment(b,d,m):
	return 6*m/(b*d**2)


print(bending_moment(1,13,4))
loadDurationFactor = {'':''}

loadlong = [['permanent',{'Cd':.9},'dead load'],['ten years',{'Cd':.9},'live load']]
temperatureFactor = 1.0 #fill out later, NDS 2.3.3
# bendingStress = M*c/I
# print(crossSectionArea_A, "what")
print(ndv.crossSectionArea_A)

woodEnum = {0:"DF",1:"HF",2:"other"}
woodDensity = {0:.5, 1:.42,3:.3}
#2.3.2
cD = {'perm':.9,'teny':1,'twom':1.15,'sevd':1.25,'tenm':1.6,'imp':2}
phivals = {'Fb' : .85, 'Ft':.8,'Fv':.75,
           'Frt':.75,'Fs':.75,'Fc':.9,
           'Fcp':.9}
#chapter 3
#----------------
#chapter three is about analyzing bending stresses on wood








print('printed')
pointload = 10
area = 10

ff = woodDensity[0]
print(ff)