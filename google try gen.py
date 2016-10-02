# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 11:26:08 2016

@author: SRINIVAS
"""

#
from bs4 import BeautifulSoup as soup
import re
import urllib.request
raw=urllib.request.urlopen('https://lgusd.powerschool.com/guardian/home.html').read()
raw=soup(raw)
print(raw)
