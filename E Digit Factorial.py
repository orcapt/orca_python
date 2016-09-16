# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 19:56:48 2016

@author: SRINIVAS
"""

import math
a=0
d=2
fro=0
o=[]
e=[]
ter=[]
q=0
we=0
quin=0
while a==0:
    o=[]
    d=d+1
    s=list(map(int,list(str(d))))
    for elem in s:
        o.append(math.factorial(elem))
    q=sum(o)
    if q==d:
        quin=q
    if quin>we:
        we=q
        ter.append(we)
        print(we)
        print(sum(ter))
        