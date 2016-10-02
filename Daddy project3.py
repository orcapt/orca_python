# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 11:54:17 2016

@author: SRINIVAS
"""

import random
import matplotlib.pyplot as plt
import numpy as np
import math
from statistics import mode
a=open('train.csv','r')
final=[]
tea=0
b=''.join(a.read()).split('\n')
b1=[]
for elem in b:
    if len(elem.split('#'))>1:
        pass
    else:
        b1.append(elem)
b=b1
print(len(b))
while tea<112000:
    tea=tea+1
    
    c=b[tea].split('"')
    try:
        listy=[c[0].split(',')[0],c[1].split(',')]
    except IndexError:
        pass
    final.append(listy)
def stats(listy):
    return([max(listy),min(listy),abs(max(listy)-min(listy)),mode(listy)])
def diff(listy):
    sed=[]
    loop=-1
    for elem in listy:
        loop=loop+1
        try:
            sed.append(listy[loop+1]-listy[loop])
        except IndexError:
            pass
    return(sed)

def exp(listy):
    a=diff(listy)
    

    a=a[1:]
    
    if sorted(a) == a:
        if a.count(a[0])!=len(a):
            return('E')
        else:
            return('L')
    else:
        return('O')
def maxi(listy):
    fin=[]
    index=0
    for elem in listy:
        index=index+1
        fin.append((listy[0:index]))
    
    return(fin)
def yay(listy):

                x=0
                ot=[]
                for elem in listy:
                    x=x+1

                    try:
                        if listy[x-1]<listy[x]:
                            pass
                        else:
                            ot.append(np.mean(listy[0:x]))
                    except IndexError:
                        pass
                return(ot)
def sort(listy):

    if sorted(listy)==listy:
        return('A')
    else:
        if sorted(listy,reverse=True)==listy:
            return('D')
        else:
            listy=yay(listy)
            if sorted(listy)==listy:
                return('oA')
            elif sorted(listy,reverse=True)==listy:
                return('oD')
            elif listy.count(listy[1])==len(listy):
                return('oC')
            else:
                return('O')


"""
for x in listy:
    if exp(x[1]):
        if x[1].index(max(x[1])):
"""

loopy=-1
finall=[]
for elem in range(0,112883):
    loopy=loopy+1
    try:
        ase=final[loopy]
    except IndexError:
        print(loopy)
        ase=final[1]
    try:
        if len(ase[1])>5:
            finall.append(exp(list(map(int,ase[1])))+sort(list(map(int,ase[1]))))
    except ValueError:
        pass
from collections import Counter
words=finall
mcommon= [ite for ite, it in Counter(words).most_common(7)]
print(mcommon)
for l in range(5):
    print(mcommon[l],(finall.count(mcommon[l])/112883))
            