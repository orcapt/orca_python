# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 08:30:20 2016

@author: SRINIVAS
"""
import matplotlib.pyplot as plt
import math
a=[]
b=-100
t=b
c=[]
d=[]
e=-1
while b<100:
    b=b+1
    
    #c.append(math.tan((b))+1.08)
    #c.append(math.tanh(math.sqrt(b))+math.sqrt(b)+7)
    c.append(math.tanh((b))+(b)+1)
    #c.append(b-1)
    #c.append(math.sin(b)*math.cos(b)-2.15*(math.tan(b))-math.sqrt(math.log10(b)))
    d.append(b)

for elem in d:
    e=e+1
    a.append(elem/c[e])
lisr=[]
for x in list(range(t,100)):
    lisr.append((x*360)/(2*3.14159265358979323846264338))
plt.plot(lisr,a)
plt.show()