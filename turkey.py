#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 19:41:47 2016

@author: Pranavtadepalli
"""

from PIL import Image
from PIL import ImageEnhance
from bs4 import BeautifulSoup as soup
import urllib.request
import webbrowser
import numpy
abc=list('turkeyTURKEY')
pies=input('Type a URL or text\n')
try:
    raw=urllib.request.urlopen(pies).read()

    soup=soup(raw,'lxml')
    raw=str(raw)
    ps=soup.find_all('p')
    f=[r.get_text() for r in ps]
    r=' '.join(f)
except:
    r=pies

filey=open('turkey.txt','a')
#r='turkey'
listy=[]
for elem in list(r):
    if elem in abc:
        listy.append(1)
    else:
        listy.append(0)
filey.write(str(listy.count(1)/len(listy))+'\n')
filey.close()
filey=open('turkey.txt','r')
file=filey.read()
real=listy.count(1)/len(listy)

number=numpy.mean(list(map(float,file.split('\n')[0:-1])))-(listy.count(1)/len(listy))
filey.close()
"""
number=number+numpy.mean(list(map(float,file.split('\n')[0:-1])))


#print(list(im.getdata())[0:100])
if abs(number)!=number:
    number=1/abs(number)
"""
im = Image.open("turkey.png")
print(real)
enhancer = ImageEnhance.Contrast(im)
enhancer.enhance((real*3.5)**1.2).show()

"""
for elem in range(2400):
    for i in range(2000):
        pixel=im.getpixel((elem,i))
        rgb=[pixel[0]*number,number*pixel[1],number*pixel[2]]
        rgb=list(map(int,list(map(round,rgb))))
        rgb=tuple(rgb)
        im.putpixel((elem,i),rgb)
im.show()
"""
        