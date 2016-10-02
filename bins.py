# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 15:43:33 2016

@author: SRINIVAS
"""
from PyDictionary import PyDictionary
import os
dictionary=PyDictionary()
a=input('text')
a=a.split(' ')
listy=os.listdir(r'C:\Users\SRINIVAS\Documents\Python Scripts')
print(listy)
def get(a):
    d=dictionary.synonym('get')
    d.append('get')
    s=set(a).intersection(d)
    if len(s)!=0:
        return(True)

print(get(a))

##not done