# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 16:39:58 2016

@author: SRINIVAS
"""
def pal(num):
    if list(str(num))==list(reversed(list(str(num)))):
        return True
    else:
        return False
listy=[]
for elem in range(0,1000000):
    if pal(elem):
        a=str(bin(elem))[2:]
        if elem==585:
            print(a)
        if pal(a):
            listy.append(elem)
print(sum(listy))
        