# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 18:18:13 2018

@author: stmwr
"""
from wooddataparser import pass_wood
from sawn_lumber_adjustments import Sawnlumberdimensions

woods = pass_wood()
   
class WoodSpecies():    
    woods = pass_wood()        
    ''' this object is the wood object information)  
    def __init__(self, e, e_main, fb, fc_par, fc_perp, ft, fv, grade, 
    size, species, sp_grav, name): #,e, fb, fc_par, fc_perp, ft, fv, grade, name, size, species):'''
    def __init__(self, name): #,e, fb, fc_par, fc_perp, ft, fv, grade, name, size, species):
        #super(wood_species, self).__init__(name)
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
        self.name = name

class WoodBeam(WoodSpecies, Sawnlumberdimensions):
    def __init__(self, name, size, length=10):
        WoodSpecies.__init__(self, name)
        Sawnlumberdimensions.__init__(self, size)
        self.length = length
    
    @property
    def selfweight(self):
        density  = 62.4 * (self.sp_grav/(1+self.sp_grav*0.19))*((1+0.19/100))
        density = round(density,2)
        return density

class WoodBeamAnalysis(WoodBeam):
    def __init__(self, name, size, length=10):
        WoodBeam.__init__(self, name, size, length)
        pass
        
    def capacity():
        print('such capacity')

    

if __name__ == "__main__":
    twood = 'ALASKA SPRUCE NO.3 2 IN. & WIDER'
    size = '4x10'
    #foo = wood_species('ALASKA SPRUCE NO.3 2 IN. & WIDER')
    #bar = wood_beam(twood, '4x12')
    baz = WoodBeamAnalysis(twood, size)
    pass
