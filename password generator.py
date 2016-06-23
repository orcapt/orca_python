# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 18:41:08 2016

@author: SRINIVAS
"""

import random
from random import randint
finalist=[]
p=''
loop=0
level=input('level 1, 2 or 3?')
char=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
numbers=[1,2,3,4,5,6,7,8,9]
stuff=['!','@',',','#','$','%','^','&','*','(',')']
ranchar=randint(0,25)
rannumbers=randint(0,8)
ranstuff=randint(0,10)
def one(ranchar,char,loop):
    while loop<8:
        loop=loop+1
        finalist.append(char[ranchar])
        ranchar=randint(0,25)
def two(ranchar,numbers,rannumbers,char,loop):
    loop=0
    while loop<10:
        loop=loop+1
        finalist.append(char[ranchar])
        ranchar=randint(0,25)
        finalist.append(str((numbers[rannumbers])))
        rannumbers=randint(0,8)
def three(ranchar,numbers,rannumbers,char,loop,ranstuff,stuff):
    loop=0
    while loop<5:
        loop=loop+1
        finalist.append(char[ranchar])
        ranchar=randint(0,25)
        finalist.append((str(numbers[rannumbers])))
        rannumbers=randint(0,8)
        finalist.append(stuff[ranstuff])
        ranstuff=randint(0,10)
if level=='2':
    two(ranchar,numbers,rannumbers,char,loop)
if level=='3':
    three(ranchar,numbers,rannumbers,char,loop,ranstuff,stuff)
if level=='1':
    one(ranchar,char,loop)
for elem in finalist:
        p=p+elem
print(p)