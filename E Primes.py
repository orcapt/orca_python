# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 14:35:59 2016

@author: SRINIVAS
"""
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 360085147514 ?
"""
import math
def primes(number):
   me=range(2,number)
   he=True
   for elem in me:
       if number%elem==0:
           he=False
   return(he)
cray=[]
m=100

way=range(3,(m))
for elem in way:
    if primes(elem):
        cray.append(elem)
for elem in cray:
    if m%elem==0:
        print(elem)