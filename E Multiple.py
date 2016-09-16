# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 13:40:02 2016

@author: SRINIVAS
"""

tree=list(range(0,1000,3))
eert=list(range(0,1000,5))
leaf=list(range(0,1000,15))
print((sum(eert)+sum(tree))-sum(leaf))