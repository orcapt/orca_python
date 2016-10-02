# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 11:16:38 2016

@author: SRINIVAS
"""

import random
import matplotlib.pyplot as plt
import numpy as np
import math
from statistics import mode
import statistics
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

print(final[1])
listolist=[]
for elem in final:
    listolist.append(elem[0])
sequences={ k[0]: k[1] for k in final }


def checkRecurrence(seq, order= 2, minlength = 7):
    """
    :type seq: List[int]
    :type order: int
    :type minlength: int 
    :rtype: List[int]
    
    Check whether the input sequence is a recurrence sequence with given order.
    If it is, return the coefficients for the recurrenec relation.
    If not, return None.
    """     
    if len(seq)< max((2*order+1), minlength):
        return None
    
    ################ Set up the system of equations 
    A,b = [], []
    for i in range(order):
        A.append(seq[i:i+order])
        b.append(seq[i+order])
    A,b =np.array(A), np.array(b)
    try: 
        if np.linalg.det(A)==0:
            return None
    except TypeError:
        return None
   
    #############  Solve for the coefficients (c0, c1, c2, ...)
    coeffs = np.linalg.inv(A).dot(b)  
    
    ############  Check if the next terms satisfy recurrence relation
    for i in range(2*order, len(seq)):
        predict = np.sum(coeffs*np.array(seq[i-order:i]))
        if abs(predict-seq[i])>10**(-2):
            return None
    
    return list(coeffs)


def predictNextTerm(seq, coeffs):
    """
    :type seq: List[int]
    :type coeffs: List[int]
    :rtype: int
    
    Given a sequence and coefficienes, compute the next term for the sequence.
    """
    
    order = len(coeffs)
    predict = np.sum(coeffs*np.array(seq[-order:]))
    return int(round(predict))
    
    
    
real=[]
    
listseq=[]
order2Seq={}   #(key, value) = (sequence id, [prediction, coefficients])
for id in sequences:  
    seq = sequences[id]
    coeff = checkRecurrence(seq,2)
    if coeff!=None:
        predict = predictNextTerm(seq, coeff)
        order2Seq[id]=(predict,coeff)

print ("We found %d sequences\n" %len(order2Seq))

for key in sorted(order2Seq):
    value = order2Seq[key]
    real.append([key, value[0]])
listseq.append(order2Seq)
for elem in range(3,100):
    exec('order'+str(elem)+'Seq={}')

    for id in sequences:
        if id in (x for x in listseq):
            continue
        seq = sequences[id]
        coeff = checkRecurrence(seq,elem)
        if coeff!=None:
            predict = predictNextTerm(seq, coeff)
            eval('order'+str(elem)+'Seq')[id]=(predict,coeff)
    
    print ("We found %d sequences\n" %len(eval('order'+str(elem)+'Seq')))
    
    listseq.append(eval('order'+str(elem)+'Seq'))
    for key in sorted(eval('order'+str(elem)+'Seq')):
        value = eval('order'+str(elem)+'Seq')[key]
        real.append([key, value[0]])
        
    
    
    
    
    
dad=[]
print(real[1])
olist=[]
print(len(olist))
print(len(real))
print(len(listolist))
for elem in real:
    olist.append(elem[0])
for elem in listolist:
    if elem not in olist:
        dad.append(elem)
print(dad[1])
print(len(dad))
other=[]
for elem in final:
    if elem[0] in dad:
        ase=elem[1]
        if len(ase)>4:
            ase1=ase[-1]
            ase.pop()
            try:
                det=mode(ase)
            except statistics.StatisticsError:
                det=ase[-1]
            if det==ase1:
                other.append(1)
print(len(other)/len(final))


