# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 13:01:15 2016

@author: PRANAV
"""
import numpy as np
etters=open('letters.txt','r+')
pie=input('Text')
final=[]
var=0

listy=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
def percent(pie,fi):
    
    pie=pie.replace(' ','')
    pie=list(pie)
    me=0
    for elem in pie:
        if elem==fi:
            me=me+1
    return((me/len(pie))*100)
    
    
meep=open('letters.txt','a')
for elem in listy:
    fi=elem
    var=percent(pie,fi)
    meep.write(elem+':'+str(var)+'\n');
meep.close()
letters=etters.read()

letters=str(letters)
letters=letters.split('\n')
fi=input('character')
for elem in letters:
    
    why=elem.split(':')
    
    if why[0]==fi:
        final.append(float(why[1]))
rice=np.mean(final)
print(rice,'%')
etters.close()
    
    
    