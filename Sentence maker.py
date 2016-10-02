# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 11:30:37 2016

@author: SRINIVAS
"""
from random import randint
inputext=input('Gimme Text!!!')
wet=open('set.txt','a')
wet.write(inputext)
wet.close()
fun=open('set.txt','r')
s=fun.read()
s=s.split(' ')
a=0
das=[]
def ire(word,h,t):
    if t==0:
        h.reverse()
        other=h.index(word)-1
        h.reverse()
    if t==1:
        other=h.index(word)+1
    
    return(s[other])
der=ire('a',s,True)
while a<100:
    
    a=a+1
    das.append(der)
    
    der=ire(der,s,randint(0,1))
wers=''
for elem in das:
    wers=wers+' '+elem

print(wers)