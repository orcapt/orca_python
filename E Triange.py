# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 19:28:26 2016

@author: SRINIVAS
"""




eo=0
me=0
ret=[]
ter=[]
while eo==0:
    ter=[]
    me=me+1
    ret.append(me)
    wer=sum(ret)
    d=list(range(1,int(wer/2)+1))
    for elem in d:
        if wer%elem==0:
            ter.append(0)
    print(len(ter))
    if len(ter)>500:
        print(wer)
        eo=9
