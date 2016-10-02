# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 16:45:09 2016

@author: SRINIVAS
"""

from bs4 import BeautifulSoup as soup
import re
import urllib.request
file=open('lastn.txt','w')
for ele in range(1,100):
    raw=urllib.request.urlopen('http://surname.sofeminine.co.uk/w/surnames/most-common-surnames-in-great-britain'+'-'+str(ele)+'.html').read()
    raw=soup(raw)
    a=raw.find_all(class_='nom')
    for elem in a:
        file.write(elem.get_text()+'\n')
file.close()