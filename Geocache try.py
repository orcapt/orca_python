# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 18:54:18 2016

@author: SRINIVAS
"""

from bs4 import BeautifulSoup as soup
import re
import urllib.request
raw=urllib.request.urlopen('http://coord.info/map?ll=37.22937,-121.95803&z=15').read()
raw=soup(raw)
gsoup1=raw
print(gsoup1)