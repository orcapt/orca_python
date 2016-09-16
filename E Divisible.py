# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 16:34:37 2016

@author: PRANAV
"""

e=list(range(1,900000))
p=list(range(1,21))
print(p)
r=0
me=0
for elem in e:
    me=True
    pier=elem
    for ele in p:
        if elem%ele==0:
            if r==1:
                me=False 
        else:
            r=1
            me=False
    if me==True:
        print(pier)
    r=0
