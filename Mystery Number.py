# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 14:24:52 2016

@author: SRINIVAS
"""

from random import randint
print('All edges must make ten')
rew=0
fire=randint(10,20)
mars=0
stoe=0

a=[0,0,0]
b=[0,0,0]
c=[0,0,0]
rete=0
while rete!=1:
    
    while rew==0:
        me=randint(1,fire-1)
        we=randint(1,fire-1)
        he=randint(1,fire-1)
        if me+we+he==fire:
            rew=1
            stoe=me
            stoe1=we
            stoe2=he
            a=[stoe,stoe1,stoe2]
    rew=0
    while rew==0:
        me=randint(1,fire-1)
        we=randint(1,fire-1)
        he=randint(1,fire-1)
        if me+we+he==fire:
            rew=1
            stoe=me
            stoe1=we
            stoe2=he
            b=[stoe,stoe1,stoe2]
    c[0]=abs(fire-(a[0]+b[0]))
    c[1]=abs(fire-(a[1]+b[1]))
    c[2]=abs(fire-(a[2]+b[2]))
    if c[0]+c[1]+c[2]==fire and c[0]!=0 and c[1]!=0 and c[2]!=0:
       
        a[1]='X'
        b[0]='X'
        b[2]='X'
        c[1]='X'
        
        print(a[0],a[1],a[2])
        print(b[0],b[1],b[2])
        print(c[0],c[1],c[2])
        rete=1

cray=-1
for elem in a:
    cray=cray+1
    a[cray]=str(elem)
cray=-1
for elem in b:
    cray=cray+1
    b[cray]=str(elem)
cray=-1
for elem in c:
    cray=cray+1
    c[cray]=str(elem)
haho=[a,b,c]
hoha=[]
for elem in haho:
    for ele in elem:
        hoha.append(ele)
import tkinter
teare=-1
c=0
root = tkinter.Tk(  )
var = tkinter.StringVar()
for r in range(3):
    for c in range(3):
        teare=teare+1
        var.set(hoha[teare])
        tkinter.Label(root, text='%s'%(var.get()),
            borderwidth=2 ).grid(row=r,column=c)
root.mainloop(  )
print(fire)
    