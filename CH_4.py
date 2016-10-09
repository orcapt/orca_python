# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 13:26:34 2016

@author: SRINIVAS
"""

from bs4 import BeautifulSoup as soup
import re
import urllib.request
t='80992'
for elem in range(401):
    raw=urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+t).read()
    
    raw=soup(raw)
    
    t=str(soup.get_text(raw).split(' ')[-1])
    print(t)