# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 19:33:09 2016

@author: pranav
"""

import itertools
"""
a=list(itertools.permutations([0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9],3))
print(-1)
meep=[]
heap=[]
for elem in a:
    meep=[]
    if elem[0]!=0:
        for elem in elem:
            meep.append(str(elem))
        meep=''.join(meep)
        heap.append(int(meep))
print(1)


m=heap
haho=m+heap

hoha=[]
b=list(itertools.permutations(haho,2))

for elem in m:
    
for elem in b:
    air=int(elem[0])*int(elem[1])
    hoha.append(air)
print(2)
cre=[]
"""
cre=[]
def pal(strin):
    strin=str(strin)
    hi=list(reversed(list(strin)))
    
    if hi==list(strin):
        return(True)
    else:
        return(False)
ger=[]
m=range(100,1000)
for elem in m:
    for ele in m:
        mul=elem*ele
        if pal(mul):
            cre.append(mul)
"""
for elem in hoha:
    if pal(elem):
        cre.append(elem)
"""
print(max(cre))
    