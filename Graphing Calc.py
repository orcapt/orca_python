
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 18:24:35 2016

@author: PRANAV
"""

import math
import matplotlib.pyplot as plt
x=range(1,int(input('Range\n')))
y1=[]
y2=[]
functionVar=input('Function\n') 
functionar=input('Function\n')
def function(x):
     return(eval(functionVar))
     
def fun(x):
     return(eval(functionar))
for number in x:
    y1.append(function(number))
for number in x:
    y2.append(fun(number))
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()
