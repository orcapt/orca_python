# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 19:42:26 2016

@author: SRINIVAS
"""

loop=0
n=0
r=0
h=0
x=0
factorial=0
j=[]
while loop<1000:
    if n==0:
        factorial=1
        # if n is zero
    r=0
    loop=loop+1
    n=n+(1/factorial)
    t=n
    n=n+1
    while h<n:
        h=h+1
        t=t-1
        j.append(t)
        #put elem in list for being mutiplied together for factorial
        while r>len(j):
            r=r+1
            #multipy all valuse in list j
            x=x*j[r-1]
            factorial=x
    if n==0:
        factorial=1
        # if n is zero
    r=0
    loop=loop+1
    n=1/factorial
    t=n
    n=n+1
print(n)

                
                
                
        
    
    