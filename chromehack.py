# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 12:23:08 2016

@author: SRINIVAS
"""

from bs4 import BeautifulSoup as soup
import re
import urllib.request
raw=urllib.request.urlopen('https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&service=mail&sacu=1&scc=1&passive=1209600&ignoreShadow=0&acui=2#Email=orca.pranav%40gmail.com').read()
raw=soup(raw)
"""raw=str(raw)

t=raw.split('\n')

loop=-1
for e in raw.split('\n'):
    loop=loop+1
    if len(e.split('pass'))>1:
        print(t[loop-1])
        print(e)
        print(t[loop+1])
"""
print(raw.find_all('input',{"name":"GALX"}))
print(raw.find_all('input',{"name":"gxf"}))