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
        zf = 1*ur.inch
        
    def itemization(self,defi,quant,unit):
        pass        
    def test():
        return 'this was returned'
    
import time

def log_calls(func):
    def wrapper(*args, **kwargs):
        now = time.time()
        print("Calling {0} with {1} and {2}".format(func.__name__, args, kwargs))
        return_value = func(*args, **kwargs)
        print("Executed {0} in {1}ms".format(func.__name__, time.time() - now))
        return return_value
    return wrapper

@log_calls
def test1(a,b,c):
    print('test 1 called')

test1(1,2,3)



if __name__ == '__main__':
    cd = notation()