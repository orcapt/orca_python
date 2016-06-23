# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 13:26:03 2016

@author: SRINIVAS
"""

number=input('choose a number that you need factors of')
number=int(number)
repeat=1
numbers=[]
while number>repeat:
    numbers.append(repeat)
    repeat=repeat+1
for elem in numbers:
    if number%elem==0:
        print(elem)
   