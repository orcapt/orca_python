# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 15:05:31 2016

@author: SRINIVAS
"""

times=0
import matplotlib.pyplot as plt
import numpy as np
x=[]
y=[]
bye=input('number')
bye=int(bye)
final=0
list1=[]
while times<bye:
    times=times+1
    list1.append(times)
for elem in list1:  
    x=elem/3
    if int(x)==x:
        final=final+1
    x=elem/5
    if x==int(x):
        final=final+1
    x==elem/15
    if x==int(x):
        final=final-1
print(final) 
