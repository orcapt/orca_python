# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 14:20:31 2016

@author: PRANAV
"""

from bs4 import BeautifulSoup as soup
import re
import urllib.request
raw=urllib.request.urlopen('http://rjfisher.lgusd.org/apps/events/').read()
raw=soup(raw)
gsoup1=raw
a=soup.get_text(gsoup1)
a=gsoup1.find_all(class_="event-day empty no-border ")
#print(soup.find(gsoup1,id="day-2",class_="event-title"))
print(a)
a=[1,1,2,3,5,8,13,21,34,55,89]
b=[1,2,3,4,5,6,7,8,9,10,11,12,13]
c=[]
for elem in a:
    if elem in b:
        if elem in c:
            dopllfrbntfhjhvbunugf=1
        else:
            c.append(elem)
for elem in c:
    print(elem)
    