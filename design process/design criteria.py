# -*- coding: utf-8 -*-

zipcode = 123 # input("what is the zipcode\n")
inputtt = zipcode
#get usgs data

Sds = zipcode
ss = zipcode
s1 = zipcode

print('what state is this design, 1 for oregon, 2 for california, 3 for washington, 4 for other')
state = input('number here: ')
if state == 1:
	print('aci-11, aisc 10, asce 10, OSSC 14, NDS-12')
if state == 2:
	print('aci-14, aisc 10, asce 10, CBC 16, NDS-15')
if state == 3:
	print('aci-14, aisc 10, asce 10, IBC 15, NDS-15')
if state == 4:
	print('figure it out')