# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 14:52:38 2016

@author: PRANAV
"""

pie=open(r'pile.txt','r')
pie=pie.read()
fi=pie.split(':')
for elem in fi:
    tree=list(elem)
    print(elem)