#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 13:16:33 2017

@author: Pranavtadepalli
"""
#'"id","qid1","qid2","question1","question2","is_duplicate"'
import csv
def quotation(string):
    return string.strip('"')
def function(q1,q2):
    county=[]
    a=q1.split(' ')
    b=q2.split(' ')
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
    if percent>.5:
        return '1'
    else:
        return '0'
data=[]
final=open('submission.csv','a')
with open('test-3.csv', newline='\n',encoding='UTF-8') as f:
    reader = csv.reader(f)
    for elem in reader:
        data.append(elem)

data=data[1:]

final.write("test_id,is_duplicate\n") 
for elem in data:
    try:
        result=function(elem[1],elem[2])
        final.write(elem[0])
        final.write(','+str(result)+'\n')
    except:
        pass
final.close()