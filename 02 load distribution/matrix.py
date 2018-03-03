#this is my start at making a matrix and power
'''
1.1 Goals:
    my goals are to be able to apply htis books
    
1.2 overview
'''

import numpy as np
def isnip(a):
    return np.array(a)
a = np.array([1+2j, 3+4j, 5+6j])
#1.8 chap 1 problems


def prob1():
    print(1,isnip(3-2j)+isnip(-7+5j))

def prob2():
    print(2,isnip(3-2j)-isnip(-7+5j))
    
def prob3():
    print(3,isnip(3-2j)*isnip(-7+5j))
    
def prob4():
    print(4,isnip(1)/isnip(1-1j))
    
def prob5():
    print(5,isnip(3-2j)/isnip(-7+5j))
    
def prob6():
    print(6,isnip(3-2j)*isnip(-7+5j))
    
def prob7():
    print(7,abs(isnip(3-2j)))
def prob8():
    print(8,abs(isnip(3-2j)))
def prob9():
    print(9,(isnip(1j)**100))
def prob10():
    print(10,(isnip(1j)**49))
def prob11():
    print(11,abs(isnip(3-2j)))
def prob12():
    print(12,abs(isnip(3-2j)))

    
    
prob1()
prob2()
prob3()

prob4()
prob5()
prob6()

prob7()
prob8()
prob9()

prob10()
prob11()
prob12()


#prob4()