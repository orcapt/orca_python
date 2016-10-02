# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 10:57:06 2016

@author: SRINIVAS
"""
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
for elem in range(3,20):
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
        