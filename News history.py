# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 17:36:26 2016

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
