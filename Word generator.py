#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 10:50:39 2017

@author: Pranavtadepalli
"""
import random

text=input('TEXT\n')
listy=list('qwertyuiopasdfghjklzxcvbnm ')
listy1=[]
for elem in listy:
    e=[]
    if elem in list(text):
        try:

            t=text.split(elem)[1:]

            for ele in t:
                listy1.append(elem+ele[0])
            
        except:
            e=[]
        
#print(listy1)
final=''
seed=random.choice(listy1)
r=0
file=open('gib.txt','w')
while True:
    newlist=[]
    final=final+seed
    r=list(seed)[-1]

    for elem in listy1:
        if elem[0]==r:
            newlist.append(elem)

    if newlist==[]:
        newlist=[random.choice(listy)+random.choice(listy)]
    seed=random.choice(newlist)[1]
    file.write(seed)
print(final)

        