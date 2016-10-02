# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 15:38:58 2016

@author: SRINIVAS
"""

from bs4 import BeautifulSoup as soup
import re
import urllib.request
import time
loop=0
while True:
    raw=urllib.request.urlopen('http://forecast.weather.gov/MapClick.php?CityName=Los+Gatos&state=CA&site=MTR&textField1=37.2267&textField2=-121.974&e=0#.V6EinbgrK00').read()
    raw=soup(raw)
    a=raw.get_text(' ').split('\n \n \n \n \n \n \n \n')[8]
    a=a[400:570]
    a=a.split('\n')[0:8]
    b=[]
    for elem in a:
        if elem==' ':
            pass
        else:
            b.append(elem)
    b.pop(1)
    files=open('Hum.txt','a')
    print(b)
    files.write(b[0]+' '+b[2]+'\n')
    files.close()
    time.sleep(3600)