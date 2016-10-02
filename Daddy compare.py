# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 20:42:13 2016

@author: SRINIVAS
"""

import random
import matplotlib.pyplot as plt
import numpy as np
import math
import statistics
from statistics import mode
list1=[]
list2=[]
list4=[]
b=open('realdad5.csv','r')
t=b.read().split('\n')
for elem in t:
    list1.append(elem)
b.close()
a=open('linearPrevious11WithModeFallback (1).csv','r')
t=a.read().split('\n')
for elem in t:
    list2.append(elem)
a.close()

c=open('justmode1.csv','r')
t=c.read().split('\n')
for elem in t:
    list4.append(elem)
c.close()

print(list1[1])
print(list2[1])


list3=[]
list3=set(list1).intersection(list2)
list3=list(set(list3) - set(list4))
print(len(list3))
