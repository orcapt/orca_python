#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 18:30:10 2016

@author: Pranavtadepalli
"""

import matplotlib.pyplot as plt
import numpy
a=list('0123456789')
b=list('1000101021')
fin=[]
for elem in range(100000):
    e=[]
    for el in list(str(elem)):
        t=a.index(str(el))
        e.append(int(b[t]))
    fin.append(numpy.mean(e))
plt.plot(list(range(100000)),fin,linewidth=0.01)
plt.show()