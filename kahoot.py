#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 15:38:14 2016

@author: Pranavtadepalli
"""

from bs4 import BeautifulSoup as soup
import random
import urllib.request
abc=list('QWERTYUIOPASDFGHJKLZXCVBNM')
for elem in range(2000):
    try:
        print(elem)
        letters=''
        for elm in [1,2,3,4,5]:
            letters=letters+random.choice(abc)
        raw=urllib.request.urlopen('https://app.nearpod.com/presentation?pin='+letters).read()
        raw=str(soup(raw))
        if len(raw)==11169:
            pass
        else:
            print("Your pin is "+letters)
    except:
        pass
