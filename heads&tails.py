# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 18:02:39 2016

@author: SRINIVAS
"""

from random import randint
t=0
s=0
l=[]
while t<100:
    t=t+1
    p=randint(0,1)
    if p==0:
        f=1
    else:
        f=0
        s=0
    while f==1:
        f=randint(0,1)
        s=s+1
    l.append(s)
d=sum(l)
a=len(l)
x=d/a
print(x)

         
        
        
