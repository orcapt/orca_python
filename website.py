# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 13:14:40 2016

@author: SRINIVAS
"""
from bs4 import BeautifulSoup as soup
import urllib.request
raw=urllib.request.urlopen('http://www.accuweather.com/en/us/san-jose-ca/95110/hourly-weather-forecast/347630').read()
gsoup=soup(raw)
print(gsoup.prettify()[0:20000])
