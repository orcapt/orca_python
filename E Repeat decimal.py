# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 12:09:43 2016

@author: SRINIVAS
"""

a=0
s=0
h=0
x=0
oh=[]
fin=[]
d=[]
t=0
while s==0:
    x=0
    d=[]
    a=a+1
    
    f=list(str((1/a)))
    f.pop(0)
    f.pop(0)
    f.pop(0)
    x=0
    for ele in f:
       x=x+1
       try:
           if f[3]==ele:
               d.append(x)
       except IndexError:
           pass
    try:
        oh=abs(d[0]-d[1])
        
    except IndexError:
        oh=0
    if oh>h:
        h=oh
        print(h,a)
        t=a
    if a==1000:
        s=2
print(h,t)
