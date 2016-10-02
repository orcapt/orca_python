# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 09:22:10 2016

@author: SRINIVAS
"""
import numpy as np
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

def sort(listy):
    if sorted(listy)==listy:
        return('A')
    else:
        if sorted(listy,reverse=True)==listy:
            return('D')
        else:
            return('O')
def maxi(listy):
    fin=[]
    index=0
    for elem in listy:
        index=index+1
        fin.append(max(listy[0:index]))
    return(fin)
def yay(listy):

                x=0
                ot=[]
                for elem in listy:
                    x=x+1
                    print(x)
                    try:
                        if listy[x-1]<listy[x]:
                            pass
                        else:
                            ot.append(np.mean(listy[0:x]))
                    except IndexError:
                        pass
                return(ot)
def diff1(listy):
    new=[listy]
    for elem in listy:
        new.append(diff(new[-1]))
    new=new[0:-1]
    print(new)
    loop=-1
    
    for elem in new:
        loop=loop+1
        if elem.count(elem[0])==len(elem):
            me=loop
    new=new[0:me]
    print(new)
    new=list(reversed(new))
    start=new[0][0]
    loop=0
    for elem in new:
        loop=loop+elem[-1]
    return(loop)


print(diff1(list(map(int,[]))))