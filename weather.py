# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 12:50:23 2016

@author: SRINIVAS
"""

from bs4 import BeautifulSoup
import urllib.request
url="http://www.accuweather.com/en/us/san-jose-ca/95110/weather-forecast/347630"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read())
print(soup)