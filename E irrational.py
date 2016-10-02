# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 09:29:16 2016

@author: SRINIVAS
"""

a=range(1,500000)
#print(''.join(str(list(a)).strip('[').strip(']').split(', ')))

numbers=''.join(map(str,list(a)))
print(len(numbers))
print(int(numbers[0])*int(numbers[9])*int(numbers[99])*int(numbers[999])*int(numbers[9999])*int(numbers[99999])*int(numbers[999999]))