'''this file will do the heavy lififting for design of beams'''
from typing import NamedTuple
import attr


@attr.s
class notation():
    pass

class units(NamedTuple):
    val: float
    defs: str
    unit: str
beamtypes = 'cantilevered, pin-pin, pin-fix, fix-fix'
beamconditions = 'simplespan, multispan'

E = {'val':0, 'def': 'modulus of elesticity', 'unit' : 'psi'}
capI = {'val': 0, 'def' : 'moment of inertia', 'unit' : 'in4'}
capL = {'val': 0, 'def' : 'length ft', 'unit' : 'ft'}
litl = {'val': 0, 'def' : 'length in', 'unit' : 'in'}
mom = {'val': 0, 'def' : 'moment', 'unit' : 'in-lbs'}
P = {'val': 0, 'def' : 'concentreated load', 'unit' : 'lbs'}
R = {'val': 0, 'def' : 'reaction load', 'unit' : 'lbs'}
V = {'val': 0, 'def' : 'shear force', 'unit' : 'lbs'}
W = {'val': 0, 'def' : 'uniform load', 'unit' : 'lbs'}
w = {'val': 0, 'def': 'load per unit length', 'unit' : 'lbs/in'}
delt = {'val': 0, 'def': 'deflectoin', 'unit': 'lbs'}
x = {'val': 0, 'def': 'dist', 'unit': 'lbs'}

class materials():
    def __init__(self):
        self.fy = fy
        self.i = i


#beam_capacity = (geomatry, materials)

E['val'] = 19000000
capI['val'] = 200
capL['val'] = 10
litl['val'] = capL['val']*12
W['val'] = 10





class simplebeamuniformload():
    def __init__(self, w, l):
        R = w * l
        M = w*l**2 * (1/8)
        delta = (5*w*l**4) / (384 * 1000 * 10000)
        self.R = R
        self.M = M
        self.delta = delta


def simplebeamuniformload_partiallydis_mid(w,l, a, b, c):
    x = l
    R1 = (w*b)*(2*c + b) / (2*l)
    R2 = (w*b)*(2*a + b) / (2 * l)
    #V at midpoint not yet calculated
    M = R1
    delta = (5*w*l**4) / (384 * 1000 * 10000)
    return R1, R2, M, delta

def simplebeamuniformload_partiallydis_oneend(w,l,a):
    x = l*.333
    R1 = (w*a)*(2*l - a) / (2*l)
    R2 = (w*a**2)/(2 * l)
    #V at midpoint not yet calculated
    Vx = R1 - w*x
    if x == R1/w:
        M = R1**2 /2*w
    if x < a:
        M = R1*x - w*x**2 / 2
        delta = (w*x) / (24*E*I*l)*(a**2*(2*l-a)**2 \
                            -2*a*x**2*(2*l-a)+l*x**3)
    if x > a:
        M = R2 ( l - x)
        delta = (w*a**2*(l-x)/ (24*E*I*l))*(4*x*l - 2*x**2 - a**2)

    return R1, R2, M, delta

def uniformloadpartiallydistributedeachend(a,b,c,w1, w2,l):
    x = l
    R1 = w1*a*(2*l-a)+w2*c**2 / (2*l)
    R2 = w2*c*(2*l-c)+w2*a**2 / (2*l)
    if R1 < w1*a:
        Mmax = R1**2 / 2*w1
    else:
        Mmax = R2 ** 2 / 2 * w2
    M = Mmax
    delta = 10
    return R1, R2, M, delta


class unit():
    def __init__(self, defs, unit, vals):
        self.units = units
        self.defs = defs
        self.vals = vals
from typing import NamedTuple
