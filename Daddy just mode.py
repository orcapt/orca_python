# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 10:02:38 2016

@author: SRINIVAS
"""

import random
import matplotlib.pyplot as plt
import numpy as np
import math
import statistics
from statistics import mode
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
        except ValueError:
            pass
    except IndexError:
        pass
    final.append(listy)
other=[]
for elem in final:
    
    ase=elem[1]
    if len(ase)>4:
        ase1=ase[-1]
        ase.pop()
        try:
            det=mode(ase)
        except statistics.StatisticsError:
            det=ase[-1]
        if det==ase1:
            other.append(1)
print(len(other)/len(final))