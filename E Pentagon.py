# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 10:45:37 2016

@author: SRINIVAS
"""

import itertools as it
n=0
wre=0
fre=0
tre=0
he=[]
e=range(1,1000)
for elem in e:
    n=n+1
    pie=(3*n)-1
    me=(n*pie)/2
    he.append(me)

tear=list(it.permutations(he,2))

for elem in tear:
    twe=elem
    re=twe[0]+twe[1]
    er=twe[0]-twe[1]
    for lem in he:
        if lem==re:
            fre=fre+1
            
        if lem==er:
            fre=fre+1
            
    if fre==2:
        print(re,er)
        print(twe[0],twe[1])
        print(abs(re-er))
    fre=0
            
