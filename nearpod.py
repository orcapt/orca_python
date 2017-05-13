#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" x
Created on Wed Nov  9 15:10:40 2016

@author: Pranavtadepalli
"""

from bs4 import BeautifulSoup as soup
import random
import urllib.request
abc=list('QWERTYUIOPASDFGHJKLZXCVBNM')
for elem in range(2000):
    print(elem)
    letters=''
    for elm in [1,2,3,4,5]:
        letters=letters+random.choice(abc)
    raw=urllib.request.urlopen('https://app.nearpod.com/presentation?pin='+letters).read()
    raw=str(soup(raw))
    if len(raw)==10822:
        pass
    else:
        print("Your pin is "+letters)
        break
