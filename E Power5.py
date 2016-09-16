# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 11:48:00 2016

@author: SRINIVAS
"""

a=0
s=0
r=[]
woo=[]
while s==0:
    a=a+1
    r=[]
    b=list(str(a))
    b=list(map(int,b))
    
    for elem in b:
        r.append(elem**5)
    
    if sum(r)==a and sum(r)!=1:
        woo.append(sum(r))
        print(sum(r),a)
        print(sum(woo))
    