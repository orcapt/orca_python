#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 14:41:23 2017

@author: Pranavtadepalli
"""
listy=[]
def divisors(number):
    

    for e in range(1,(number//2)+1):
        if number%e==0:
            yield e
            
print(list(divisors(18)))

for elem in range(10000):
    num=sum(list(divisors(elem)))
    num1=sum(list(divisors(num)))
    if num1==elem:
        if num!=num1:
            listy.append((num,num1))
tr=[]
print(listy)
t=0
for elem in listy:
    if t==0:
        tr.append(elem[0])
        tr.append(elem[1])
    if t==0:
        t=1
    else:
        t=0
print(sum(tr))