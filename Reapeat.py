# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 16:59:10 2016

@author: SRINIVAS
"""
from statistics import mode
import statistics
seq=list(input('seq').split(','))
seat=list(set(seq))
seqj=''.join(seq)
real=[]
for elem in seat:
    final=[]
    split=seqj.split(elem)
    for ele in split:
        final.append(elem+ele+elem)
        final.append(ele+elem)
        final.append(elem+ele)
    for eem in final:
        real.append(eem)
o=[]
for elm in real:
    if list(set(seqj.split(elm)[1:-1]))==['']:
        o.append(elm)
try:
    print(mode(o))
except statistics.StatisticsError:
    try:
        print(o[0])
    except IndexError:
        print('No pattern detected')
