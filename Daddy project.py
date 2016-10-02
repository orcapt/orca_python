# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 17:23:22 2016

@author: SRINIVAS
"""
import random
import matplotlib.pyplot as plt
a=open('train.csv','r')
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
while tea<112000:
    tea=tea+1
    
    c=b[tea].split('"')
    try:
        listy=[c[0].split(',')[0],c[1].split(',')]
    except IndexError:
        pass
    final.append(listy)
print(len(final))
for elem in range(0,100):
    ase=final[random.randint(1,110000)]
    print(ase[1])
    print('ID #'+str(ase[0]))
    print('Plot #'+str(elem))
    plt.plot(list(range(len((ase[1])))),list(ase[1]))
    plt.scatter(list(range(len((ase[1])))),list(ase[1]))
    plt.show()