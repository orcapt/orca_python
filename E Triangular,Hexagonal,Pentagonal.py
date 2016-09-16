# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 21:47:13 2016

@author: PRANAV
"""
from collections import Counter
e=[]
f=[]
g=[]
n=0
ho=0
while ho<2000000:
    ho=ho+1
    n=n+1
    b=n+1
    t=(n*b)/2
    e.append(t)
    b=(3*n)-1
    p=(n*b)/2
    f.append(p)
    b=(2*n)-1
    h=n*b
    g.append(h)

print(list((Counter(e) & Counter(g) & Counter(f)).elements()))