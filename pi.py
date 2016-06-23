# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 18:35:28 2016

@author: SRINIVAS
"""
x=-1
p=-3
pie=[]
t=0
h=0
r=0
q=0
g=0
u=2
while h<1000:
    h=h+1
    p=p+4
    t=4/p 
    a=4/(2+p)
    i=t-a
    pie.append(i)
while r<len(pie)-1:
    r=r+1
    q=q+1
    f=pie[len(pie)-(len(pie)-q)]
    g=g+f
print(g)
    
    
 
        
        