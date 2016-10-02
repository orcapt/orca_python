# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 08:31:02 2016

@author: SRINIVAS
"""
from PyDictionary import PyDictionary
dictionary=PyDictionary()
from statistics import mode
from statistics import StatisticsError
a=open('set.txt','r')
ase=a.read()
a.close()
t=ase.split('.')
fee=[]
sent=[]
for elem in t:
    fee=[]
    tre=elem.split(' ')
    for eem in tre:
        if eem!='' and eem!='/n':
            fee.append(eem)
    sent.append(fee)
l=[]
real=[]
var=0
for elem in sent:
    l=[]
    var=0
    for ele in elem:
        fr=dictionary.meaning(ele)
        try:
            fr=list(fr.keys())
            try:
                l.append(mode(fr))
            except StatisticsError:
                l.append(fr[0])
            print(l)
        except AttributeError:
            var=1
    if var==0:
        real.append(l)
        


        
    