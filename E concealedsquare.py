# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 15:52:15 2016

@author: SRINIVAS
"""
import math
import itertools
#a=list('1_2_3_4_5_6_7_8_9_0')
#t=itertools.combinations('1234567890',9)
a=list('1_2_3_4_5_6_7_8_9_0')
t=itertools.permutations('0123456789',9)
lists=[]
for elem in t:
    r=[]
    loop=0
    for ele in a:

        if ele=='_':
            r.append(elem[loop])
            loop=loop+1
        else:
            r.append(ele)
    r=''.join(r)

    if (float(math.sqrt(int(r)))).is_integer():
        print(r)

