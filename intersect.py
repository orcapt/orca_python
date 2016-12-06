#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 20:40:58 2016

@author: Pranavtadepalli
"""
#method 1
a=[1,2,3,4,5,5,5,6]
c=[]
b=[1,2,55,6,3,4,6,6]
for elem in a:
    for ele in b:
        if elem==ele:
            c.append(ele)
print(list(set(c)))
#method 2
def intersect(a,b):
    r=[]
    for x in a:
        if x in b:
            r.append(x)
    return(r)