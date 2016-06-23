# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 14:38:50 2016

@author: SRINIVAS
"""

times=0
final=0
splitpie=0
list1=[]
list3=[]
list5=[]
while times<1001:
    times=times+1
    list1.append(times)
for elem in list1:
    
    x=elem/3
    if x==int:
        final=final+1
    splitpie=str(elem).split()
    last=splitpie[-0]
    last=int(last)
    if last==5 or 0:
        final=final+1
        
        
    