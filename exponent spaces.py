# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 19:13:07 2016

@author: SRINIVAS
"""

pie=range(1,52)
red=0
cod=0
pe=[]
teel=0
blue=0
team=[]
def fun(pie,red):
    me=[]
    fin=[]
    for elem in pie:
        
        me.append(elem**red)
    t=0
    for elem in me:
        t=t+1
        try:
            fin.append(me[t]-elem)
        except IndexError:
            pass
    return(fin)
def dist(pie):
    fin=[]
    t=0
    for elem in pie:
        t=t+1
        try:
            fin.append(pie[t]-elem)
        except IndexError:
            pass
    return(fin)
print(dist(fun(pie,2)))
while cod<10:
    cod=cod+1
    blue=fun(pie,cod+1)
    
    while teel<cod:
        teel=teel+1
        
        blue=dist(blue)
    team.append(blue)
    teel=0
for elem in team:
    pe.append(elem[1])
print(pe)