# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 17:14:56 2016

@author: SRINIVAS
"""

sentence=input('sentence')
sentence=sentence.split(' ')
loopvar=0
pie=""
loopyvar=0
new=[]
for elem in sentence:
    loopyvar=loopyvar+1
while loopvar<loopyvar:
    loopvar=loopvar+1
    new.append(sentence[-1])
    sentence.pop()
for elem in new:
    pie=pie+elem+' '
print(pie)