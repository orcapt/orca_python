# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 17:04:17 2016

@author: SRINIVAS
"""

def primes(number):
   me=range(2,number)
   he=True
   for elem in me:
       if number%elem==0:
           he=False
   return(he)


rad=[]
red=0
beehive=1
while red==0:
    beehive=beehive+1
    if primes(beehive):
        rad.append(beehive)
    if len(rad)==10001:
        red=10
print(rad[-1])
