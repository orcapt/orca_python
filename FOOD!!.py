# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 14:33:07 2016

@author: SRINIVAS
"""

from bs4 import BeautifulSoup as soup
import re
import urllib.request

raw=urllib.request.urlopen('http://rjfisher.lgusd.org/apps/pages/index.jsp?uREC_ID=221140&type=d&pREC_ID=515466').read()
raw=soup(raw)
a=raw.find_all('a')
listy=[]
for elem in a:

    #if len(elem.split('Wednesday Flyer'))==2:
    #    print(elem)
    if len(str(elem).split('Wednesday Flyer'))==2:
        listy.append(str(elem))
print(listy[1].split('"')[1])
"""
b=raw.find_all('a')
for elem in b:
    print(elem.get_text())
"""
