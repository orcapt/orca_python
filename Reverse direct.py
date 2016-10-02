# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:14:39 2016

@author: SRINIVAS
"""

import matplotlib.pyplot as plt
a=[]
for x in range(100):
    a.append(x*5+2)
    #a.append(x/2)
    a.append(0.01+x/2)
    #a.append(x*115)

b=[]
c=[]
loop=-1
for elem in a:
    b.append(float(''.join(reversed(list(str(elem))))))


plt.plot(a,b)
