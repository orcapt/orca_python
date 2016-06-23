# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 16:26:44 2016

@author: SRINIVAS
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for elem in a:
    if elem>5:
        print(elem,'is greater than five')
    else:
        if elem==5:
            print(elem, 'is equal to five')
        else:
            print(elem,'is less than five')