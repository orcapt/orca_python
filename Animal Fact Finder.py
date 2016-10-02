# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 11:10:47 2016

@author: SRINIVAS
"""

from bs4 import BeautifulSoup as soup
import re
import urllib.request
derf=input('Animal?')
raw=urllib.request.urlopen('https://www.britannica.com/animal/'+derf).read()
raw=soup(raw)
me=raw.get_text().split('\n')
print(max(me, key=len))