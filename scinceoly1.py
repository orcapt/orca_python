# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 18:26:31 2016

@author: SRINIVAS
"""

from bs4 import BeautifulSoup as soup
from random import choice
import urllib.request
from PyDictionary import PyDictionary
from nltk.corpus import words
dictionary=PyDictionary()
abc=list('qwertyuiopasdfghjklzxcvbnm')
raw=urllib.request.urlopen('https://www.brainpop.com/science/seeall/').read()
raw=soup(raw)
raw=str(raw)
raw=raw.split(',')
listy=[]
for elem in raw:
    if len(elem.split('{"name"'))==2:
        tr=elem.split(':')[1]
        tre=tr.strip('"')
        listy.append(tre)
listy=listy[3:-1]
fin2=[choice(abc),choice(abc),choice(abc),choice(abc)]
fin1=[' ',choice(listy),choice(listy),choice(listy),choice(listy)]


file=open('science.csv','w')
file.write(','.join(fin1))

for elem in fin2:
    file.write('\n')
    file.write(elem+',')
