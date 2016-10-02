# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 16:53:29 2016

@author: SRINIVAS
"""
import math
import matplotlib.pyplot as plt
x=range(1,25)
y=[]
"""
def function(x):
    loop=0
    def primes(number):
        me=range(2,number)
        he=True
        for elem in me:
            if number%elem==0:
                he=False
        return(he)
    d=range(x)
    for elem in d:
        if primes(elem):
            loop=loop+1
    return(loop)
"""
def function(x):
    davar=x
    haha=0
    sequence=[0,1]

    def fib(sequence):
        sequence.append(sequence[-1]+sequence[-2])
    
    while haha<davar:
        haha=haha+1
        fib(sequence)
    return(sequence[-1])           
for number in x:
    y.append(function(number))
plt.plot(x,y)
plt.show()
