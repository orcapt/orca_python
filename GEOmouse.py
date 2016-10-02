# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 11:35:14 2016

@author: SRINIVAS
"""

from bs4 import BeautifulSoup as soup
import re
import urllib.request
raw=urllib.request.urlopen('http://mynasadata.larc.nasa.gov/latitudelongitude-finder/').read()
raw=soup(raw)
print(raw.get_text())