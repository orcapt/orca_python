# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 22:22:55 2016

@author: SRINIVAS
"""

import numpy as np
import matplotlib.pyplot as plt



def diff(listy):
    sed=[]
    loop=-1
    for elem in listy:
        loop=loop+1
        try:
            sed.append(listy[loop+1]-listy[loop])
        except IndexError:
            pass
    return(sed)

y=[2,64,64*32,64*32**2,64*32**3]

x=[1,2,3]
yn=diff(y)
ynn=diff(yn)
cof=np.polyfit(x,ynn,1)
print(cof)
x.append(4)
yon=np.polyval(cof,x)
yon=list(map(int,list(map(round,yon))))
print(yn[-1])
plt.plot(yon)
plt.plot(ynn)
print(yon,ynn)
plt.show()