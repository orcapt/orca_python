# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 14:48:40 2016

@author: SRINIVAS
"""

me=0
tea=0
gee=True
listy=list(range(1,21))      #list of numbers 1-20
print(listy)

while me==0:                 
    gee=True
    tea=tea+20     #            
    
    for elem in listy:
        if tea%elem!=0:
            gee=False
    if gee==True:
        me=1
        print(tea)
