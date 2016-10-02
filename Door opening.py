# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 18:32:01 2016

@author: SRINIVAS
"""
import matplotlib.pyplot as plt
a=open('door.txt','r')
me=a.read()
a.close()
AverageA2=[1]
AverageA=[1]
AreaA=[1]
AreaA2=[1]
me=me.split('\n')
for elem in me:
    b=elem.split(':')
    if b[0]=='Area A':
        AreaA.append(float(b[1]))
    if b[0]=='Area A^2':
        AreaA2.append(float(b[1]))
    if b[0]=='Average A':
        AverageA.append(float(b[1]))
    if b[0]=='Average A^2':
        AverageA2.append(float(b[1]))

plt.plot(AverageA2)
plt.show()
plt.plot(AverageA)
plt.show()
plt.plot(AreaA2)
plt.show()
plt.plot(AreaA)
plt.show()