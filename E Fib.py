# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 14:21:37 2016

@author: SRINIVAS
"""

davar=input('how many numbers for your fibonnaci sequence?')
davar=int(davar)
haha=0
ter=[]
sequence=[0,1]

def fib(sequence):
    sequence.append(sequence[-1]+sequence[-2])
    
while haha<davar:
    haha=haha+1
    if sequence[-1]<4000000:
        fib(sequence)
sequence.pop()
sequence.pop(0)
sequence.pop(1)
for elem in sequence:
    if elem%2==0:
        ter.append(elem)
print(sum(ter))