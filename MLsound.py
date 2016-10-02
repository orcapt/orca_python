# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 20:37:01 2016

@author: SRINIVAS
"""
import time
a=[]
me=open('sound.txt','a')
#te=open('time.txt','w')
#at=open('time.txt','r')
#et=at.read()
#print(et)
e=open('sound.txt','r')
em=e.read()
em=str(em)

em=e.readlines()
em=e.split('\n')
for elem in em:
    a.append(elem)

pie=et
me.close()
te.close()
at.close()
e.close()

"""
pie=int(pie)


for elem in a:
    if elem==' ':
        time.sleep(pie)
    else:
        print('\a')
cat=int(input(''))
if cat<0:
    te.write(et-abs(cat/10))
if cat>0:
    te.write(et+(cat/10))
"""