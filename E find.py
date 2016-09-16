# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 11:26:12 2016

@author: SRINIVAS
"""
from bs4 import BeautifulSoup as bs
import urllib.request
t=[]
we=0
url='https://projecteuler.net/problem='
meep=input('Problem #')
url=url+meep
page = urllib.request.urlopen(url)
soup = bs(page.read())
tea=soup.findAll('p')
for elem in tea:
    print(bs.get_text(elem))
    