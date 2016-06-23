# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 20:43:00 2016

@author: SRINIVAS
"""
t=0
l=1
o=1
r=1
fo=-1
x=0
d=-1
pi=3
op=[]
nope=[]
pie=[]
while t<90:
    l=l+1
    pie.append(l)
    t=t+1
while  fo<88:
    d=d+1
    fo=fo+1
    r=r+1
    if r==2:
        x=4
    else:
        x=3
    if d/x==int:
        fd=op[1]*op[0]*op[2]
        int(fd)
        nope.append(4/fd)
        del op[:]
    else:
        o=r
        op.append(o)
        
nope.append(3)
print(nope)
pi=sum(nope)
print(pi)
        
    
    