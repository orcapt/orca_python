# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 13:27:49 2016

@author: SRINIVAS
"""

from bs4 import BeautifulSoup as soup
import urllib.request
raw=urllib.request.urlopen('http://finance.yahoo.com/q?s=AAPL').read()
raw=soup(raw)
gsoup1=raw
fi=gsoup1.find_all(class_="yfnc_tabledata1")
print(fi[0])
print(fi[7])
print(fi[8])
print(fi[11])
my=(str(fi[0]))
my=my.split('>')[1]
print(my.split('<')[0],'was the stock price of apple yesterday')
