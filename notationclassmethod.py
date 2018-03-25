# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 19:31:28 2018

@author: stmwr
"""

import pint
ur = pint.UnitRegistry()

class notation:
    def __init__(self, defi = 'what', quant =1*ur('')):       
        self.defi = defi
        self.quants = quant.magnitude
        self.unit = quant.units
    def __repr__(self):
        return f'this is the {self.defi}'
    def __call__(self):
        print('called')  
    def __mul__(self, other):
        zz = 1*ur('in')
        zf = 1*ur.
        
    def itemization(self,defi,quant,unit):
        pass        
    def test():
        return 'this was returned'

if __name__ == '__main__':
    cd = notation()
    cd
    