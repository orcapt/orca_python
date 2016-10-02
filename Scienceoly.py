# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 18:07:25 2016

@author: SRINIVAS
"""

from bs4 import BeautifulSoup as soup

import urllib.request
from PyDictionary import PyDictionary
from nltk.corpus import words
dictionary=PyDictionary()

raw=urllib.request.urlopen('http://sci2.esa.int/glossary/').read()
raw=soup(raw)
t=raw.find_all('a')
ate=[]
for lee in t:
    if len(lee.get_text())<3:
        pass
    else:
        ate.append(lee.get_text())
ate=ate[1:-1]
re=[]
for elem in ate:
    if len(elem.split('('))<2:
        if len(elem.split(' '))<2:
            if len(elem.split('-'))<2:
                re.append(elem)
print(re)
    