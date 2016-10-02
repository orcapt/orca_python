# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 13:25:57 2016

@author: SRINIVAS
"""

from random import randint
print('All edges must make ten')
rew=0
creek=randint(0,2)
wertq=randint(0,2)
frim=randint(0,2)
mars=0
stoe=0

def fun(e,heat):
     eat=-1
     
     for elem in e:
         eat=eat+1
         if heat==eat:
             e[eat]='X'
a=[0,0,0]
b=[0,0,0]
c=[0,0,0]
rete=0
while rete!=1:
    
    while rew==0:
        me=randint(1,9)
        we=randint(1,9)
        he=randint(1,9)
        if me+we+he==10:
            rew=1
            stoe=me
            stoe1=we
            stoe2=he
            a=[stoe,stoe1,stoe2]
    rew=0
    while rew==0:
        me=randint(1,11)
        we=randint(1,5)
        he=randint(1,7)
        if me+we+he==10:
            rew=1
            stoe=me
            stoe1=we
            stoe2=he
            b=[stoe,stoe1,stoe2]
    c[0]=abs(10-(a[0]+b[0]))
    c[1]=abs(10-(a[1]+b[1]))
    c[2]=abs(10-(a[2]+b[2]))
    if c[0]+c[1]+c[2]==10 and c[0]!=0 and c[1]!=0 and c[2]!=0:
       
        fun(a,creek)
        fun(b,wertq)
        fun(c,frim)
        
        print(a[0],a[1],a[2])
        print(b[0],b[1],b[2])
        print(c[0],c[1],c[2])
        rete=1
