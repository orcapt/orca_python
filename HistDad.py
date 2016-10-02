# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 14:48:30 2016

@author: SRINIVAS
"""

import random
import matplotlib.pyplot as plt
import numpy as np
import math
from statistics import mode
a=open('train.csv','r')
final=[]
tea=0
b=''.join(a.read()).split('\n')
b1=[]
for elem in b:
    if len(elem.split('#'))>1:
        pass
    else:
        b1.append(elem)
b=b1

while tea<112000:
    tea=tea+1
    
    c=b[tea].split('"')
    try:
        listy=[c[0].split(',')[0],c[1].split(',')]
    except IndexError:
        pass
    final.append(len(listy[1]))
print(max(final))
plt.hist(final,bins=5000)
plt.show()