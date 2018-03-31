#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 15:56:40 2017

@author: sean
"""
#import pprintp
import constants
import csv


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


def pass_wood():
    return woods

#writes all wood items to single dict
woods = {}
for j in range(len(i)):
    aab = list(zip(i[0][1:],i[j][1:]))
    props = {aab[i][0]:aab[i][1] for i in range(0,len(aab))}
    woods[i[j][0]] = props


i=j=k=row=props= aab =zz= rr=None
   
with open("Output.txt", "w") as text_file:
    text_file.writelines(woods)
    
    
class wood_species(object):
    name = object
    def __init__(self, name): #,e, fb, fc_par, fc_perp, ft, fv, grade, name, size, species):
        self.e = woods[name]['E']
        self.e_min = woods[name]['EMIN']
        self.fb = woods[name]['FB'] 
        self.fc_par = woods[name]['FC_PAR'] 
        self.fc_perp = woods[name]['FC_PERP'] 
        self.ft = woods[name]['FT']
        self.fv = woods[name]['FV']
        self.grade = woods[name]['GRADE']
        self.size = woods[name]['SIZE']
        self.species = woods[name]['SPECIES']
        self.sp_grav = woods[name]['SP_GRAV']
    def __call__(self):
        return f'the species is {self.species}'

class wood_beam(object):
    def __init__(self,object):
        wood_species.__init__(self, object.e, object.e_min, object.fb, object.fc_par, object.fc_perp, object.ft, object.fv, \
                              object.grade, object.size, object.species, object.sp_grav)
        spec_name = 'WHITE OAK STANDARD'
        size = '2x4'
        if size == '2x4':
            b = 2
            d = 4
        #self.species = wood_species(spec_name)
        self.spanlength = 10 #10 feet

class wood_column(object):
    def __init_(self, Emin, CM, Ct, CT, Ci, Cr):
        self.Emin= woodspecies.Emin()
        self.CM=  CM
        self.Ct=  Ct
        self.CT=  CT
        self.Ci=  Ci
        self.Cr=  Cr
    def  GetAdjustedMinModulusOfElasticity():
        EminPrime = Emin * CM * Ct * Ci * CT        
        return EminPrime

class SawnLumberMemberAdjustment():
    def __init__(self):
        self.F_b = 1
        self.C_M_Fb = 1
        self.C_t_Fb = 1
        self.C_L =1
        self.C_F_Fb = 1
        self.C_fu_Fb = 1
        self.C_i_Fb = 1
        self.C_r = 1
        self.lambd = 12
    
    def getAdjustedBendingDesignValue(F_b, C_M_Fb, C_t_Fb, \
                                      C_L, C_F_Fb, C_fu_Fb, \
                                      C_i_Fb, C_r, lambd):
        phi = 0.85 #; //Table 4.3.1
        K_f = 2.54 #; //Table 4.3.1
        F_b_prime = self.F_b * phi * K_f * self.lambd * self.C_M_Fb * \
                    self.C_t_Fb * self.C_L * self.C_F_Fb * self.C_fu_Fb *\
                    self.C_i_Fb * self.C_r
        return F_b_prime
        
    def GetAdjustedCompressionDesignValue( F_c, C_M_Fc, C_t_Fc, C_F_Fc, C_i_Fc, C_P, lambd):
        phi = 0.9 #; //Table 4.3.1
        K_f = 2.4 #; //Table 4.3.1
        F_c_prime = F_c*phi * K_f * lambd * C_M_Fc * C_t_Fc *  C_F_Fc * C_i_Fc * C_P
        return F_c_prime

    def GetAdjustedShearDesignValue( F_v, C_M_Fv, C_t_Fv, C_i_Fv, lambd):
        phi = 0.75 #; //Table 4.3.1
        K_f = 2.88 #; //Table 4.3.1
        F_v_prime = F_c * phi * K_f * lambd * C_M_Fv * C_t_Fv *  C_i_Fv
        return F_v_prime
        
    def GetAdjustedTensionValue( F_t, C_M_Ft, C_t_Ft, C_F_Ft, C_i_Ft, lambd):
        phi = 0.8 #; //Table 4.3.1
        K_f = 2.7 #; //Table 4.3.1
        F_t_prime = F_t * phi * K_f * lambd * C_M_Ft * C_t_Ft * C_F_Ft * C_i_Ft
        return F_t_prime
    
    def GetAdjustedModulusOfElasticity( E, C_M, C_t_E, C_i):
        E_prime = E * C_M * C_t_E * C_i #;  //from Table 4.3.1
        return E_prime
        
    def GetAdjustedMinimumModulusOfElasticityForStability( E_min, C_M_E, C_t_E, C_i_E, C_T):
        K_F = 1.76;
        phi = 0.85;
        E_min_prime = E_min * C_M_E * C_t_E * C_i_E * C_T * K_F * phi #; //from Table 4.3.1
        return E_min_prime;
        

        
if __name__ == "__main__":
    twood = 'ALASKA SPRUCE NO.3 2 IN. & WIDER'
    foo = wood_species('ALASKA SPRUCE NO.3 2 IN. & WIDER')
    bar = wood_beam(foo)
    pass
