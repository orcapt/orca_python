# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 21:11:25 2016

@author: SRINIVAS
"""

import random
import matplotlib.pyplot as plt
import numpy as np
import math
from statistics import mode
import statistics
a=open('test.csv','r')
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
print(len(b))
while tea<len(b)-1:
    tea=tea+1
    
    c=b[tea].split('"')
    try:
        try:
            listy=tuple([int(c[0].split(',')[0]),list(map(int,c[1].split(',')))])
            final.append(listy)
        except ValueError:
            pass
    except IndexError:
        pass

print(len(final))