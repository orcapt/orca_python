# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 16:31:35 2016

@author: SRINIVAS
"""

from bs4 import BeautifulSoup as soup
import re
import urllib.request
raw=urllib.request.urlopen('http://imesart.com/connect.php').read()
raw=soup(raw)
print(raw)