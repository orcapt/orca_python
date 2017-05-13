#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 18:19:03 2017

@author: Pranavtadepalli
"""

def divisors(number):
    
    lis=[]
    for e in range(1,(number//2)+1):
        if number%e==0:
            lis.append(0)
    return len(lis)+1
t=0
loop=0
looplist=[]
while t==0:
    loop=loop+1
    looplist.append(loop)
    triangle=sum(looplist)
    divs=divisors(triangle)
    print(divs)
    if divs>500:
        print(triangle)
        t=1