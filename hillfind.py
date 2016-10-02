# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 18:23:50 2016

@author: PRANAV
"""
#
from bs4 import BeautifulSoup as soup
import re
import urllib.request
raw=urllib.request.urlopen('http://bh.lgusd.org/apps/staff/').read()
raw=soup(raw)
gsoup1=raw
f=0
erde=0
hay=input('Type the last name of the teacher you want. \n')
#print(gsoup1.find_all(class_="user-data"))
#print(soup.find(gsoup1,id="staff[75]-name"))
a=soup.get_text(gsoup1)
a=a.split('\n')
#print(a)

for elem in a:
    if f!=0:
        f=f-1
        print(elem)
    if re.search(hay, elem, re.M|re.I):
        ri=elem.split(' ')
        for ele in ri:
            if erde==0:
                if re.search(hay, ele, re.M|re.I):
                    f=f+5
                    erde=1