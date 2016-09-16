# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 13:49:56 2016

@author: SRINIVAS
"""

def primes(number):
   me=range(2,number)
   he=True
   for elem in me:
       if number%elem==0:
           he=False
   return(he)
   
   
   
pie=range(1,500)
pie1=range(1,500)
pie2=range(1,500)
for elem in pie:
    for elem1 in pie1:
        for elem2 in pie2:
            if elem<elem1<elem2:
                if elem+elem1+elem2==1000:
                    if (elem**2)+(elem1**2)==elem2**2:
                        print(elem1*elem*elem2)

"""
cer=0
orca=1
free=0
while cer==0:
    orca=orca+2
    free=primes(orca)
    if free:
        a=orca
        b=((a**2)/2)-0.5
        c=((a**2)/2)+0.5
        if (a**2)+(b**2)==c**2:
            print(a+b+c)
            if a+b+c==1000:
                cer=10
                print(a*b*c)
"""