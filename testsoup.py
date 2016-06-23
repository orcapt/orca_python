# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 15:31:19 2016

@author: SRINIVAS
"""
from bs4 import BeautifulSoup as soup
import urllib.request
raw=urllib.request.urlopen('http://finance.yahoo.com/q?s=AAPL').read()
raw=soup(raw)
gsoup1=raw
pie=-1
print(gsoup1.find_all(class_="yfnc_tabledata1")
'''
gsoup2=gsoup1.split(' ')
#print(gsoup1)

#for elem in gsoup2:
#    fi=elem.split('<')
#    if pie==0:
#        pie=-1
 #       print(elem)
#    try:
#       if fi[0]=='width="48%">Prev Close:':
#           pie=pie+1
#          print('yay')
#  except IndexError:
'''