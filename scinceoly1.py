 # -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 18:26:31 2016

@author: PRANAV
"""

from bs4 import BeautifulSoup as soup
from random import choice
import urllib.request
from PyDictionary import PyDictionary
import webbrowser
dictionary=PyDictionary()
abc=list('wertyuiopasdfghjklcvbnm')
raw=urllib.request.urlopen('https://www.brainpop.com/science/seeall/').read()
raw=soup(raw,'lxml')
raw=str(raw)
raw=raw.split(',')
listy=[]
for elem in raw:
    if len(elem.split('{"name"'))==2:
        tr=elem.split(':')[1]
        tre=tr.strip('"')
        listy.append(tre)
listy=listy[3:-1]
filere=open('catogories1.txt','r').read()

for lee in filere.read().split('\n'):
    listy.append(lee)
listy=filere.readlines()

filere.close()
for elem in listy:
    print(elem)
print(len(listy))
fin2=[choice(abc),choice(abc),choice(abc),choice(abc),choice(abc)]
while len(set(fin2))!=5:
    fin2=[choice(abc),choice(abc),choice(abc),choice(abc),choice(abc)]
fin1=[' ',choice(listy),choice(listy),choice(listy),choice(listy),choice(listy)]


file=open('science.csv','w')
file.write(','.join(fin1))

for elem in fin2:
    file.write('\n')
    file.write(elem+',')
file.close()
import os
os.system("open /Users/Pranavtadepalli/PythonStuff/science.csv")

webbrowser.open('/Users/Pranavtadepalli/PythonStuff/science.csv')