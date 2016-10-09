# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 16:27:32 2016

@author: SRINIVAS
"""

from bs4 import BeautifulSoup as soup
import urllib.request

raw=urllib.request.urlopen('https://www.brainpop.com/science/seeall/').read()
raw=soup(raw)
a=raw.find_all(href=True)