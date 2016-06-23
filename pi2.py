# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 12:45:14 2016

@author: SRINIVAS
"""

j=0
pi=0
o=0
while j<500000:
    j=j+1
    if j%2==0:
        o=1
    else:
        o=-1
    pi=pi-(o/(j*(j+1)*(2*j+1)))
 #   print(pi)
pi=pi+3
print(pi)