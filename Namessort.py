# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 17:06:29 2016

@author: SRINIVAS
"""

a=open('lastn.txt','r')
r=a.readlines()
a.close()
g=[]
for e in r:
    g.append(''.join(list(e[0:-3])))
r=g
in1='a'
in2=30
r.append(in1)
r.sort()

per=r.index(in1)
print(per)
per=per/len(r)
print(per)
per=per*int(in2)
print(per)
    
    