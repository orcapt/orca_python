# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 21:31:00 2016

@author: SRINIVAS
"""

from PyDictionary import PyDictionary
dictionary=PyDictionary()
in1=input('letter')
in2=input('sentence')
in2=in2.split(' ')
final=[]
final1=[]
abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for pie in abc:
    final=[]
    for elem in in2:
        var=elem
        try:
            for leme in dictionary.synonym(elem):
                if list(leme)[0]==pie:
                    var=leme
        except TypeError:
            var=elem
        
        final.append(var)
    final1.append(' '.join(final))
nextlist=[]
nextlist1=[]
counts=[]
high=[0,0]
for elm in final1:
    nextlist=elm.split(' ')
    nextlist1=[]
    counts=[]
    for elem in nextlist:
        nextlist1.append(elem[0])
    for elem in nextlist1:
        counts.append(nextlist1.count(elem))
    if max(counts)>high[0]:
        high=[max(counts),elm]
print(high[1])
    