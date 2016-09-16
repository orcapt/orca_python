# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 12:05:24 2016

@author: SRINIVAS
"""

import itertools
b=[]
e=''
a=itertools.permutations([0,1,2,3,4,5,6,7,8,9],10)
for elem in a:
    me=map(str,elem)
    d=''.join(me)
    b.append(int(d))
    
b.sort()

print(b[999999])
    
