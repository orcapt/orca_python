# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 20:38:33 2016

@author: SRINIVAS
"""

from bs4 import BeautifulSoup as soup
import re
import urllib.request
input1=input('Search')
raw=urllib.request.urlopen('https://www.bing.com/search?q='+'+'.join(input1.split(' '))).read()
raw=soup(raw)
#print(soup.get_text(raw))
urls=[]
t=raw.find_all(href=True)
for elem in t:
    elem=str(elem)
    try:
        if len(elem.split('www.'))>1:
            if len(elem.split('blog'))>1 or len(elem.split('src'))>1:
                pass
            else:
                if len(input1.split(' '))>1:
                     urls.append(elem.split('"')[3])
                else:
                    if len(elem.split(input1))>1:
                        urls.append(elem.split('"')[3])
    except:
        pass
#print(urls)
texts=[]
for eem in urls:
    try:
        raw=urllib.request.urlopen(eem).read()
        raw=soup(raw)
        for elem in raw.find_all('p'):
            texts.append(soup.get_text(elem))
    except:
        pass
yum=[]
for le in texts:
    el=le.split('\n')
    for elem in el:
        if len(elem.split(input1))>1:
            print(elem)
                
        