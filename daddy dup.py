# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 19:56:10 2016

@author: SRINIVAS
"""

def list_duplicates(seq):
  seen = set()
  seen_add = seen.add
  # adds all elements it doesn't know yet to seen and all other to seen_twice
  seen_twice = set( x for x in seq if x in seen or seen_add(x) )
  # turn the set into a list (as requested)
  return list( seen_twice )
  
import random
import matplotlib.pyplot as plt
import numpy as np
import math
from statistics import mode
import statistics
a=open('test2.csv','r')
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
            listy=tuple([int(c[0].split(',')[0])])
            final.append(listy)
        except ValueError:
            pass
    except IndexError:
        pass
    

listolist=[]
for elem in final:
    listolist.append(elem[0])
    
    
print(list_duplicates(listolist))