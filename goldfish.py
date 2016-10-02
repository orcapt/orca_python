# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 10:14:45 2016

@author: PRANAV
"""

goldfish=input('name?')
goldfish=list(goldfish)
redfish=goldfish
a=0
deep=''
silverfish=[]
for letter in goldfish:
    a=a+1
    silverfish.append(redfish[-a])
for letter in silverfish:
    deep=deep+letter
print(deep)