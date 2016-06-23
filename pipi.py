# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 10:57:06 2016

@author: SRINIVAS
"""
j=-1
pi=0
o=0
while j<5000000:
    j=j+1
    if j%2==0:
        o=1
    else:
        o=-1
    pi=pi+(o)/(2*j+1)
pi=4*pi
print(pi)
    