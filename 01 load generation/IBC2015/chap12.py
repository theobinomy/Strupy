# -*- coding: utf-8 -*-

class beam(x,y):
    def __init__(self,x,y):
        print('what')
        self.x = x
        self.y = y
    def __repr__(self):
        return 'whos this'
    def __str__(self):
        return f'when what {x} {y}'
        
eggs = beam('sfd','adf')
print(eggs(1,2))


def beam1():
    length = 10
    EI = 29000000
    rho = .5
