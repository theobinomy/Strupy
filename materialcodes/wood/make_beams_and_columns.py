# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 18:18:13 2018

@author: stmwr
"""

from materialcodes.wood.wooddataparser import WoodSpecies, ur
from materialcodes.wood.sawn_lumber_adjustments import Sawnlumberdimensions
import physics.beamdesign


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

class WoodBeamAnalysis(WoodBeam, physics.beamdesign.simplebeamuniformload):
    def __init__(self, name:str, size:str, w_, length=10):
        WoodBeam.__init__(self, name, size, length)
        physics.beamdesign.simplebeamuniformload.__init__(self, w_, length)
        pass

    def __repr__(self):
        return f'WoodBeamAnalysis method'
    def __str__(self):
        return 'analysis method for wood beam'

    def capacity(self):
        print('such capacity')

    def momdcr(self):
        momap = self.M / self.s_x
        dcr = momap / self.Fb
        dcr.ito_base_units()
        print(dcr)
        return dcr

if __name__ == "__main__":
    twood = 'ALASKA SPRUCE NO.3 2 IN. & WIDER'
    size = '2x8'
    #foo = wood_species('ALASKA SPRUCE NO.3 2 IN. & WIDER')
    #bar = wood_beam(twood, '4x12')
    baz = WoodBeamAnalysis(twood, size, 12 * ur.lbf / ur.foot, 8*ur.feet)
    cr = baz.momdcr()
    pass
