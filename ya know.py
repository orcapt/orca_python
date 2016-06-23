# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 20:01:22 2016

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
    b=0
    x=elem/3
    if int(x)==x:
        x=elem/5
        if x!=int(x):
            final=final+1
            y.append(final)
            b=1
            
    if x==int(x):
        final=final+1     
        y.append(final)
        b=1
    if b==0:
        y.append(0)
x=list1
plt.scatter(x,y)
plt.show()
print(final) 
