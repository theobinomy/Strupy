#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 15:56:40 2017

@author: sean
"""
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

#writes all wood items to single dict
woods = {}
for j in range(len(i)):
    aab = list(zip(i[0][1:],i[j][1:]))
    props = {aab[i][0]:aab[i][1] for i in range(0,len(aab))}
    woods[i[j][0]] = props

i= j= k= row= props= aab= zz= rr= None
   
with open("Output.txt", "w") as text_file:
    text_file.writelines(woods)
    
def pass_wood():
    return woods
 
