# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 16:58:04 2016

@author: SRINIVAS
"""

e=[]
a=list(range(1,101))
for elem in a:
    e.append(elem**2)
me=sum(e)
tree=sum(a)**2
print(abs(me-tree))


    