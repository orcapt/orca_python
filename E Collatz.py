# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 21:11:26 2016

@author: SRINIVAS
"""

x=1
v=0
tear=0
orc=[]
while x<1000000:
    x=x+1
    orc=[x]
    while orc[-1]!=1:
        
        if orc[-1]%2==0:
            me=orc[-1]/2
        else:
            me=(3*orc[-1])+1
        orc.append(me)
    
    if len(orc)>v:
        v=len(orc)
        print(v)
        tear=x
print(tear)