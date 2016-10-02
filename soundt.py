# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 18:37:48 2016

@author: SRINIVAS
"""

import winsound
from random import randint as ran
from random import choice
winsound.Beep(6000, 100)
a=ran(200,1000)
b=ran(200,1000)
c=ran(200,1000)
d=a=ran(100,500)
e=a=ran(200,1000)
a1=ran(100,500)
a2=ran(100,3000)
a3=ran(100,3000)
b1=[]
choiceA=[]
choiceB=[]
choiceC=[]
def A(a1,a2,a3,a,b,c,d,e):
    aas=[a1,a2,a3]
    oos=[a,b,c,d,e]
    choiceA=[]
    for elem in range(ran(2,7)):
        choiceA.append([choice(aas),choice(oos)])
    return(choiceA)
At=A(a1,a2,a3,a,b,c,d,e)
Bt=A(a1,a2,a3,a,b,c,d,e)
Ct=A(a1,a2,a3,a,b,c,d,e)

def aa(b1,At):
    for elem in At:
        b1.append(elem)
        print(elem)
def ba(b1,Bt):
    for elem in Bt:
        b1.append(elem)
def ca(b1,Ct):
    for elem in Ct:
        b1.append(elem)
Aw=aa(b1,At)
Bw=ba(b1,Bt)
Cw=ca(b1,Ct)
print(At)
print(At)

Aw
Aw
Aw
Aw




for elem in b1:
    winsound.Beep(elem[0],elem[1])

