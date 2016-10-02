# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 17:19:22 2016

@author: SRINIVAS
"""

import filemapper as fm
files=fm.load('Mom Proj')
fileslist=[]
for elem in files:
    fileslist.append(elem.split('_'))
fileslistr=[]
for elem in fileslist:
    elem[-1]=elem[-1].split('.')[0]
    fileslistr.append(elem)
print(fileslistr)
loop=-1 
final=[] 
for f in files:
    e=[]
    loop=loop+1
    for i in fm.read(f):
        d=','.join(fileslistr[loop])
        e.append(d+','+i)
    final.append(e)
import csv

loop=-1
for elem in final:
    loop=loop+1
    name=str(''.join(fileslistr[loop]))+'1'+'.csv'
    myfile = open(name, 'w')
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for ele in elem:
        wr.writerow(ele.split(','))