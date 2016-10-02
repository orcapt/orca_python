# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 10:28:56 2016

@author: SRINIVAS
"""

from bs4 import BeautifulSoup as soup

import urllib.request
srt=input('What word?')
raw=urllib.request.urlopen('http://www.rhymezone.com/r/rhyme.cgi?typeofrhyme=perfect&Word='+srt).read()
raw=soup(raw)
a=raw.find_all('b')
pie=[]
re=[]
ret=[]
for elem in a:
    pie.append(elem.get_text())
pie=pie[3:-6]
for elem in pie:
    defr=elem.split('\xa0')
    defr=' '.join(defr)
    ret.append(defr)
    
get='  '.join(ret)
ase=get.split('syllables')
per=0
for elem in ase:
    per=per+1
    print(per)
    print(elem[0:-2],'\n')

