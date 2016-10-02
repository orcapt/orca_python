# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 15:12:56 2016

@author: SRINIVAS
"""

import random
import matplotlib.pyplot as plt
import numpy as np
import math
from functools import reduce
from fractions import gcd
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
oos=[]

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
                
                

def diff1(listy):
    pie=listy
    awe=[]
    d=reduce(gcd,listy)
    for elem in listy:
        awe.append(elem/d)
    listy=awe
    new=[listy]
    old=[pie]
    for elem in listy:
        new.append(diff(new[-1]))
    for elem in listy:
        old.append(diff(old[-1]))
    new=new[0:-1]
    old=old[0:-1]
    loop=-1
    oth=0
    for elem in new:
        loop=loop+1
        if elem.count(elem[0])==len(elem):
            me=loop
            oth=1
    if oth==1:
        old=old[0:me]
        old=list(reversed(old))
        start=new[0][0]
        loop=0
        for elem in old:
            loop=loop+elem[-1]
        return(loop)
    else:
        return(mode(pie))



"""
for x in listy:
    if exp(x[1]):
        if x[1].index(max(x[1])):
"""

loopy=-1
finall=[]
for elem in range(0,100000):
    loopy=loopy+1
    ase=final[loopy]
    if len(ase[1])>5:
        try:
            if exp(list(map(int,ase[1])))+sort(list(map(int,ase[1])))=='EA': #change EA to liking
                oos.append(ase)
        except ValueError:
            pass
ids1=[]
loopvar=-1
fungi=[]
for elem in range(99000):
    loopvar=loopvar+1
    #plt.scatter(range(len(oos[loopvar][1])),diff(diff(oos[loopvar][1])))
    
    #plt.plot(oos[loopvar
    #print(diff(diff(oos[loopvar][1])))
    try:
        som=oos[loopvar][1]
        a=som[-1]
        del som[-1]
        b=diff1(list(map(int,som)))
        if str(a)==str(b):
            fungi.append(1)
            ids1.append(oos[loopvar][0])
        #print(oos[loopvar][0])
        #plt.yscale('log')
        #plt.show()
    except IndexError:
        pass

print(len(fungi)/loopvar)
#print(ids1[0:1000])