# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 22:53:10 2016

@author: SRINIVAS
"""

import numpy as np
import matplotlib.pyplot as plt
from statistics import mode
import statistics

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

#y=[2,64,64*32,64*32**2,64*32**3]
y=[]

def linear(y):
    x=list(range(1,len(y)+1))
    xp=6
    yn=diff(y)
    ynn=diff(yn)
    cof=np.polyfit(x,y,1)
    #print(cof)
    
    yon=np.polyval(cof,x)
    
    newlist=0
    newlist2=0
    loop=-1
    for elem in y:
        loop=loop+1
        newlist=newlist+(elem-yon[loop])**2
        newlist2=newlist2+(elem-np.mean(y))**2
    newlist=(1-newlist/newlist2)*100
    predict=np.polyval(cof,xp)
    
    if newlist<99:
        try:
            predict=mode(y)
        except statistics.StatisticsError:
            predict=y[-1]
    yon=list(map(int,list(map(round,yon))))
    #print(yn[-1])
    #plt.plot(yon)
    #plt.plot(y)
    #print(yon,y)
    return(round(float(predict)))
    #plt.show()
print(linear(y))