# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 18:18:13 2018

@author: stmwr
"""
from wooddataparser import pass_wood

woods = pass_wood()
   
class wood_species():
    
    ''' this object is the wood object information)  
    def __init__(self, e, e_main, fb, fc_par, fc_perp, ft, fv, grade, 
    size, species, sp_grav, name): #,e, fb, fc_par, fc_perp, ft, fv, grade, name, size, species):'''
    def __init__(self, woods, name): #,e, fb, fc_par, fc_perp, ft, fv, grade, name, size, species):
        self.e =       woods[name]['E']
        self.e_min =   woods[name]['EMIN']
        self.fb =      woods[name]['FB'] 
        self.fc_par =  woods[name]['FC_PAR'] 
        self.fc_perp = woods[name]['FC_PERP'] 
        self.ft =      woods[name]['FT']
        self.fv =      woods[name]['FV']
        self.grade =   woods[name]['GRADE']
        self.size =    woods[name]['SIZE']
        self.species = woods[name]['SPECIES']
        self.sp_grav = woods[name]['SP_GRAV']
        #self.name = name

class wood_beam():
   pass

class wood_column(object):
    def __init_(self, Emin = 1, CM = 1, Ct = 1, CT = 1, Ci = 1, Cr=1 ):
        self.Emin= woodspecies.Emin()
        self.CM=  CM
        self.Ct=  Ct
        self.CT=  CT
        self.Ci=  Ci
        self.Cr=  Cr
    def  GetAdjustedMinModulusOfElasticity():
        EminPrime = Emin * CM * Ct * Ci * CT        
        return EminPrime

class fish():
    def __init__(self, first, last, skel = 'hard'):
        self.first = first
        self.last = last

class trout(fish):
    pass

if __name__ == "__main__":
    twood = 'ALASKA SPRUCE NO.3 2 IN. & WIDER'
    #foo = wood_species(woods,'ALASKA SPRUCE NO.3 2 IN. & WIDER')
    #bar = wood_beam(foo)
    pass
