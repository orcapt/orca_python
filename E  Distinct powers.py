# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 14:28:08 2016

@author: SRINIVAS
"""

a=list(range(2,101))
b=list(range(2,101))
ha=[]
for leme in a:
    for elem in b:
        ha.append(leme**elem)

print(len(list(set(ha))))