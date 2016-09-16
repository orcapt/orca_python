# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 14:35:59 2016

@author: SRINIVAS
"""
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number  ?
"""
import math
#Function check if number is a divisor of big number and if is a prime. Returns true if both requirments are met
def primes(number):
   me=range(2,number)
   he=True
   for elem in me:
       if number%elem==0:
           
           he=False
   if 600851475143%number!=0:
       he=False
       
   return(he)
   
me=int(math.sqrt(600851475143))
#iterates through me numbers and prints prime factors of big num
for elem in range(3,me,2):
    if primes(elem):
        print(elem)

"""
cray=[]

m=360085147514
m1=1000

way=range(3,m1)

for elem in way:
    if primes(elem):
        cray.append(elem)

print (cray)
"""   
