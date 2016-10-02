# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 08:41:23 2016

@author: SRINIVAS
"""

import random
import matplotlib.pyplot as plt
import numpy as np
import math
import statistics
from statistics import mode
a=open('test.csv','r')
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
while tea<len(b)-1:
    tea=tea+1
    
    c=b[tea].split('"')
    try:
        try:
            listy=tuple([int(c[0].split(',')[0]),list(map(int,c[1].split(',')))])
        except ValueError:
            pass
    except IndexError:
        pass
    final.append(listy)
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

def linear(y):
    try:
        x=list(range(1,len(y)+1))
        xp=6
        yn=diff(y)
        ynn=diff(yn)
        cof=np.polyfit(x,y,1)
        #print(cof)
        
        yon=np.polyval(cof,x)
        
        newlist=0
        newlist2=0
        loop=-1
        for elem in y:
            loop=loop+1
            newlist=newlist+(elem-yon[loop])**2
            newlist2=newlist2+(elem-np.mean(y))**2
        newlist=(1-newlist/newlist2)*100
        predict=np.polyval(cof,xp)
        
        if newlist<80:
            """
            try:
                predict=mode(y)
            except statistics.StatisticsError:
                predict=y[-1]
        yon=list(map(int,list(map(round,yon))))
        """
            predict=0
    except OverflowError:
        """
        try:
            predict=mode(y)
        except statistics.StatisticsError:
            predict=y[-1]
        """
        predict=0
        #yon=list(map(int,list(map(round,yon))))
    #print(yn[-1])
    #plt.plot(yon)
    #plt.plot(y)
    #print(yon,y)
    return(round(float(predict)))
    #plt.show()

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
a.close()
counts=[]
for elem in final:
    
    tret=elem[1]
    if len(tret)>4:
        tre=tret[-1]
        tret.pop()
        if int(linear(tret))==int(tre):
            counts.append(1)
print(len(counts)/len(final))
    