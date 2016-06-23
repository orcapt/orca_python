# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 15:58:30 2016

@author: SRINIVAS
"""

from bs4 import BeautifulSoup
import urllib.request
url="http://www.google.com/finance?cid=22144"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read())
universities=soup.findAll('p',class_='')
print(universities)