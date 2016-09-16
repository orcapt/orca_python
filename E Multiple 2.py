# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 18:34:36 2016

@author: SRINIVAS
"""
"""
import math
i=range(2,int(math.sqrt(600851475143)))
for elem in i:
    x=600851475143/elem
print(x)
"""
def primes(number):
   me=range(2,number)
   he=True
   for elem in me:
       if number%elem==0:
           
           he=False
   if 600851475143%number!=0:
       he=False