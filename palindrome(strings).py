# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 14:16:45 2016

@author: SRINIVAS
"""
sting=input('palindrome?')
string=list(sting)
var=0
new=[]
while var<len(sting):
    var=var+1
    new.append(string[-1])
    string.pop()
if list(sting)==new:
    print('that is a big old palindrome')
else:
    print('not a palindrome')