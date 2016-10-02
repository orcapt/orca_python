# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 11:14:28 2016

@author: SRINIVAS
"""

from bs4 import BeautifulSoup as soup
import re
import urllib.request
fut=0
while fut<20:
    fut=fut+1
    raw=urllib.request.urlopen('https://geoiptool.com/').read()
    raw=soup(raw)
    gsoup=raw.find_all('span')
    me=[]
    for elem in gsoup:
        me.append(elem.get_text())
    me=''.join(me)
    me=me.split('Latitude')[-1]
    me=me.split(':')
    t=[]
    for elem in me:
        t.append(elem.split('Longitude')[0])
    t=t[1:3]
    print(t)