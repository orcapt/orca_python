# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 11:04:46 2016

@author: SRINIVAS
"""
from bs4 import BeautifulSoup as soup
import urllib.request
import random
from nltk.corpus import words

raw=urllib.request.urlopen('http://www.totallystupid.com/?what=3').read()
raw=soup(raw)
me=raw.findAll('td',text=True)
fee=[]
for elem in me:
    fee.append(elem.get_text())
fee=fee[0:-3]
oof=[]
for elem in fee:
    if elem.isupper():
        pass
    else:
        oof.append(elem)

ba2=['','','']
ba3=['','','']
a=0
funn=0
yy=0
yay=0
while funn==0:
    print(0)
    top=random.choice(oof)
    ba1=list(top)
    while a==0:
        sed=random.choice(oof)
        if list(sed)[0]==ba1[0]:
            ba2[0]=list(sed)[1]
            ba3[0]=list(sed)[2]
            a=1
    a=0
    while a==0:
        sed=random.choice(oof)
        if list(sed)[0]==ba1[1]:
            ba2[1]=list(sed)[1]
            ba3[1]=list(sed)[2]
            a=1
    a=0
    while a==0:
        sed=random.choice(oof)
        if list(sed)[0]==ba1[2]:
            ba2[2]=list(sed)[1]
            ba3[2]=list(sed)[2]
            a=1
    a=0
    if ''.join(ba2) in words.words():
        yay=1
    if ''.join(ba3) in words.words():
        yy=1
    if yy==1 and yay==1:
        funn=1
print(ba1[0],ba1[1],ba1[2])
print(ba2[0],ba2[1],ba2[2])
print(ba3[0],ba3[1],ba3[2])

