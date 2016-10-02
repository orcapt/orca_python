# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 20:55:09 2016

@author: PRANAV
"""

from bs4 import BeautifulSoup as soup
import urllib.request
raw=urllib.request.urlopen('http://rjfisher.lgusd.org/apps/pages/index.jsp?uREC_ID=377946&type=u&pREC_ID=494105').read()
raw=soup(raw)
gsoup1=raw
f=0
(print(gsoup1.find_all(class_="faux-figure")))