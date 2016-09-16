# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 20:44:27 2016

@author: SRINIVAS
"""

print(''.join(list(str(sum(list(map(int,open('50n.txt','r').read().split('\n'))))))[0:10]))


