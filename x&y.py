# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 19:58:53 2016

@author: SRINIVAS
"""

import matplotlib.pyplot as plt
import numpy as np
slope=0
constant=0
yes=input("do you want to plot a straight line or a parabula? s=straight line and p=parabula")
if yes=="s":
    constant=input('What would you like your constant to be')
    slope=input('What is your slope')
    constant=int(constant)
    slope=int(slope)
    x=[0,1,2,3,4,5]
    y=[constant,constant+slope,constant+slope*2,constant+slope*3,constant+slope*4]
else:
    a=input('What would you like a to be?')
    c=input('What would you like c to be?') 
    b=input('What would you like b to be?')
    a=int(a)
    c=int(c)
    b=int(b)
    x=[0,1,2,3,4,5]
    y=[c,a*1**2+b*1+c,a*2**2+b*2+c,a*3**2+b*3+c,a*4**2+b*4+c]
plt.plot(y)
