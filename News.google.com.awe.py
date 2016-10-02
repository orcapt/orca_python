# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 17:25:51 2016

@author: SRINIVAS
"""

from bs4 import BeautifulSoup as soup
import re
import urllib.request
a=open('newsinfo.txt','a')
a.close()

raw=urllib.request.urlopen('https://news.google.com/news/section?cf=all&pz=1&topic=tc&siidp=cd52eeb616dbd07075a0fd7b0d4871a5c847&ict=ln').read()
raw=soup(raw)
pea=raw.find_all(class_='titletext')
ohhh=[]
for elem in pea:
    ohhh.append(elem.get_text())

sed=input('Search?\n')
real=[]
for elem in sed.split(' '):
    if len(elem)<3:
        pass
    else:
        real.append(elem)

loop=[]
loo=[]
fut=0
for elem in ohhh:
    
    loop=[]
    for ele in real:
        if ele in elem.split(' '):
            loop.append(0)
            
    if len(loo)<len(loop):
        loo=loop
        fut=elem
print(fut)
