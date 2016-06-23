# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:16:49 2016

@author: SRINIVAS
"""
open_file = open('names.txt', 'r')
file=open_file.read()
open_file.close()
file=file.split()
lea=0
luke=0
darth=0
for elem in file:
    if elem=='Lea':
        lea=lea+1
    if elem=='Luke':
        luke=luke+1
    if elem=='Darth':
        darth=darth+1
print('It says luke',luke,'times')
print('It says lea',lea,'times')
print('It says darth',darth,'times')