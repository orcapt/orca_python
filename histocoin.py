# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 21:46:33 2016

@author: SRINIVAS
"""
from random import choice
import matplotlib.pyplot as plt
import numpy as np

t=0
w=[]
u=[]
k=[]
jk=[]
s=0
tot=0
trials=100000
l=[]
def boolean():
     return choice((1,0))
while t<trials:
    t=t+1
    p=boolean()
#    print  (p)
    if p==1:
        f=1
    else:
        f=0 
        s=0
    while f==1:
        f=boolean()
#        print (f)
        s=s+1
    tot=tot+s    
    l.append(s)
#    print (l)
    s=0
d=sum(l)
a=len(l)
x=d/a
#x=tot/trials
print(x)

plt.hist(l, bins=10, normed=True)
plt.show()


    if elem==0:
        w.append(1)
    
we=sum(w)
for elem in l:
    if elem==1:
        u.append(1)
ue=sum(u)

for elem in l:
    if elem==2:
        k.append(1)
ke=sum(k)
for elem in l:
    if elem==3:
        jk.append(1)
jke=sum(jk)


n_groups = 2

means_men = (we,ue,ke,jk)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, means_men, bar_width,
                 alpha=opacity,
                 color='b',
                 error_kw=error_config)



plt.xlabel('Number')
plt.ylabel('Number of Numbers')

plt.xticks(index + bar_width, ('0', '1', '2', '3', '4'))
plt.legend()

plt.tight_layout()
plt.show()