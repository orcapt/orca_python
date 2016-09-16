# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 15:44:48 2016

@author: SRINIVAS
"""
listy=[]
for a in range(100):
    for b in range(100):
        listy.append(sum(list(map(int,list(str(a**b))))))
print(max(listy))