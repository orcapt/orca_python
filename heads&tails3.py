# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 19:25:29 2016

@author: SRINIVAS
"""

from random import choice
t=0
s=0
tot=0
trials=100000
l=[]
def boolean():
     return choice((1,0))
while t<trials:
    t=t+1
    p=boolean()
#    print  (p)
    if p==1:
        f=1
    else:
        f=0 
        s=0
    while f==1:
        f=boolean()
#        print (f)
        s=s+1
    tot=tot+s    
    l.append(s)
#    print (l)
    s=0
d=sum(l)
a=len(l)
x=d/a
#x=tot/trials
print(x)

