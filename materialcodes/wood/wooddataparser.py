#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 15:56:40 2017

@author: sean
"""
import csv
import pint
ur = pint.UnitRegistry(system = 'imperial')


#creates list of datafile
i = []
with open('NDS_Design_Values6.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        i.append(row)

#make all items in file uppcercase     
for zz in range(len(i[0])):
    i[0][zz] = i[0][zz].upper()
for zz in range(len(i[1])):
    i[1][zz] = i[1][zz].upper()
for rr in range(len(i)):
    i[rr][0] = i[rr][0].upper()
#converts numbers to floats
for j in range(len(i)):
    for k in range(len(i[0])):
        try:
            i[j][k] = float(i[j][k])
        except ValueError:
            pass

#writes all wood items to single dict
woods = {}
for j in range(len(i)):
    aab = list(zip(i[0][1:],i[j][1:]))
    props = {aab[i][0]:aab[i][1] for i in range(0,len(aab))}
    woods[i[j][0]] = props

i= j= k= row= props= aab= zz= rr= None
   
with open("Output.txt", "w") as text_file:
    text_file.writelines(woods)
    
def pass_wood():
    return woods
 
class WoodSpecies():
    ''' this object is the wood object information)
    def __init__(self, e, e_main, fb, fc_par, fc_perp, ft, fv, grade,
    size, species, sp_grav, name): #,e, fb, fc_par, fc_perp, ft, fv, grade, name, size, species):'''
    def __init__(self, name):
        self.E =       woods[name]['E'] * ur.psi
        self.Emin =   woods[name]['EMIN'] * ur.psi
        self.Fb =      woods[name]['FB'] * ur.psi
        self.Fc_par =  woods[name]['FC_PAR'] * ur.psi
        self.Fc_perp = woods[name]['FC_PERP'] * ur.psi
        self.Ft =      woods[name]['FT'] * ur.psi
        self.Fv =      woods[name]['FV'] * ur.psi
        self.grade =   woods[name]['GRADE']
        self.size =    woods[name]['SIZE']
        self.species = woods[name]['SPECIES']
        self.sp_grav = woods[name]['SP_GRAV'] * ur.dimensionless
        self.name = name