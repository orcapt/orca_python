# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 19:25:29 2016

@author: SRINIVAS
"""

from random import choice
t=0
s=0
l=[]
def boolean():
     return choice((1,0))
while t<10:
    t=t+1
    p=boolean()
    print  (p)
    if p==1:
        f=1
    else:
        f=0 
        s=0
    while f==1:
        f=boolean()
        print (f)
        s=s+1
    l.append(s)
    print (l)
    s=0
d=sum(l)
a=len(l)
x=d/a
print(x)