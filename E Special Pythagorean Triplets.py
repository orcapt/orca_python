# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 14:24:59 2016

@author: PRANAV
"""

pie=0
ads=0
lister=[]
listy=[]
it=[]
fin=[]
ert=int(input('number'))
while pie<ert:
    pie=pie+1
    lister.append(pie)
for elem in lister:
    ti=list(str(elem))
    for ele in ti:
        it.append(int(ele))
    if sorted(it)==it or sorted(it,reverse=True)==it:
        fin.append('not bouncy')

    else:
        fin.append('bouncy')
    it=[]
for elem in fin:
    if elem=='bouncy':
        ads=ads+1
print((ads/len(fin))*100,'% bouncy')