#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 09:41:51 2016

@author: Pranavtadepalli
"""
import matplotlib.pyplot as plt
import numpy as np
from random_words import RandomWords
rw = RandomWords()
vow=list('aeiou')
x=[]
y=[]

t=[]
for elem in range(10000):
        #print(word)
        o=0
        word = rw.random_word()
        for e in list(word):
            if e in vow:
                o=o+1
        try:
            y.append((len(word)-o)/o)
            x.append(len(word))
            t.append([x[-1],y[-1],word])
        except:
            print(word)
"""
print(12)
for elem in x:
    for elm in y:
        th=str(int(elem))+str(int(elm))+'=[]'
        exec('o'+th)
print(21)
for l in t:
    for r in t:
        #print(l)
        if l[0]==r[0]:
            if l[1]==r[1]:
                eval('o'+str(int(l[0]))+str(int(l[1]))).append(l[2])
fins=[]
print('po')
for elem in x:
    for elem in y:
        try:
            k=eval('o'+str(int(elem))+str(int(elm)))
            if len(k)!=0:
                fins.append(list(set(k)))
        except:
            pass

print(fins)
"""
plt.scatter(x,y)
#plt.show()
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
plt.show()