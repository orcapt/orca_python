# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 12:43:24 2016

@author: PRANAV
"""

pie=input('Text')
fi=input('character')

def percent(pie,fi):
    pie=pie.replace(' ','')
    pie=list(pie)
    me=0
    for elem in pie:
        if elem==fi:
            me=me+1
    return((me/len(pie))*100)
print(percent(pie,fi),'%')