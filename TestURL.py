#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 22:53:38 2016

@author: Pranavtadepalli
"""

from bs4 import BeautifulSoup as soup

import urllib.request
raw=urllib.request.urlopen('https://en.wikipedia.org/wiki/Beetle').read()

raw=soup(raw)
print(raw)