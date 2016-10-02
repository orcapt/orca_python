# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 13:46:02 2016

@author: SRINIVAS
"""

a1=[0,0,0,0]
a2=[0,0,0,0]
a3=[0,0,0,0]
a4=[0,0,0,0]
win=0
def cord(a1,a2,a3,a4):
    pie=int(input('cordx'))
    pie1=int(input('cordy'))
    number=int(input('what number would you like to put there'))
    if pie==0:
        pie=a1
    if pie==1:
        pie=a2
    if pie==2:
        pie=a3
    if pie==3:
        pie=a4
    pie[pie1]=number
def check(a1,a2,a3,a4):
    ha=0
    nork=[a1,a2,a3,a4]
    for elem in nork:
        ha=ha+1
        if sum(elem)==10:
            if elem[1]!=0 and elem[2]!=0 and elem[0]!=0 and elem[3]!=0:
                return(1)
    b1=[a1[0],a2[0],a3[0],a4[0]]
    b2=[a1[1],a2[1],a3[1],a4[1]]
    b3=[a1[2],a2[2],a3[2],a4[2]]
    b4=[a1[3],a2[3],a3[3],a4[3]]
    if 0 not in b1:
        if sum(b1)==10:
            return(1)
    if 0 not in b2:
        if sum(b2)==10:
            return(1)
    if 0 not in b3:
        if sum(b3)==10:
            return(1)
    if 0 not in b4:
        if sum(b4)==10:
            return(1)
print(a1)
print(a2)
print(a3)
print(a4)
while win==0:
        print('player 1 turn')
        cord(a1,a2,a3,a4)
        print(a1)
        print(a2)
        print(a3)
        print(a4)
        if check(a1,a2,a3,a4)==1:
            print('player 1 won')
            win=1
        print('player 2 turn')
        cord(a1,a2,a3,a4)
        print(a1)
        print(a2)
        print(a3)
        print(a4)
        if check(a1,a2,a3,a4)==1:
            if win==0:
                print('player 2 won')
                win=1
        