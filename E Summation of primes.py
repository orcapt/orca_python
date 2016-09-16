# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 14:28:37 2016

@author: SRINIVAS
"""

def primes(number):
   me=range(2,number)
   he=True
   for elem in me:
       if number%elem==0:
           he=False
   return(he)


re=0
f=1
l=[]
while re==0:
    f=f+1
    
    if primes(f):
        l.append(f)
        print(f)
    if f==1999999:
        re=1
print(sum(l))
