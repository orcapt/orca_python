# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 18:44:32 2016

@author: SRINIVAS
"""

from bs4 import BeautifulSoup as soup
import re
import urllib.request
raw=urllib.request.urlopen('http://www.colorhexa.com/color-names').read()
raw=soup(raw)
gsoupy=raw.find_all('td')
me=0
for elem in gsoupy:
    me=me+1
    if me%9==0:
        try:
            print(int(elem.get_text()))
        except ValueError:
            print(elem.get_text())
        