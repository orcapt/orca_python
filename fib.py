# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 16:56:21 2016

@author: SRINIVAS
"""

davar=input('how many numbers for your fibonnaci sequence?')
davar=int(davar)
haha=0
sequence=[0,1]

def fib(sequence):
    sequence.append(sequence[-1]+sequence[-2])
    
while haha<davar:
    haha=haha+1
    fib(sequence)
print(sequence)