#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 12:37:02 2017

@author: Pranavtadepalli
"""
#'"id","qid1","qid2","question1","question2","is_duplicate"'
import numpy
raw=open('train.csv',encoding='utf-8').read().split("\n")
data=[]
masterdup=[]
masterdif=[]
def quotation(string):
    return string.strip('"')
for elem in raw:
    data.append(list(map(quotation,elem.split(','))))
for elem in data:
    try:
        county=[]
        a=elem[3].split(' ')
        b=elem[4].split(' ')
        c=[]
        c.extend(a)
        c.extend(b)
        for word in c:
            if word in a:
                if word in b:
                    county.append(1)
            else:
                county.append(0)
        percent=county.count(1)/len(county)
        if elem[5]=='1':
            masterdup.append(percent)
        if elem[5]=='0':
            masterdif.append(percent)
    except:
        print('error')
print(numpy.mean(masterdif))
print(numpy.mean(masterdup))