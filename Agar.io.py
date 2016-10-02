# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 10:52:37 2016

@author: SRINIVAS
"""
from bs4 import BeautifulSoup as soup
import webbrowser
#import random
import urllib.request
input1=input('Search wikipedia\n')
raw=urllib.request.urlopen('https://en.wikipedia.org/wiki/'+input1).read()
raw=soup(raw)
gsoup1=raw
a=gsoup1.find_all(name='img')
urls=[]
for elem in a:
    urls.append(elem.get('src'))
real=[]
for elem in urls:
    if len(elem.split(input1))>=2:
        real.append(elem)  
file=open('ih.html','w')
file.write('<!doctype html>')
file.write('\n')
file.write('<html>')
file.write('\n')
file.write('<body>')
file.write('\n')
file.write('<h1>'+str.upper(input1)+'</h1>')
file.write('\n')
fier=0
pile=len(urls)
for elem in real:
    file.write(r'<img src="'+'https:'+elem+'">')
    file.write('\n')
file.write('</body>')
file.write('\n')
file.write('</html>')
file.write('\n')
file.close()
ber=webbrowser.get('windows-default')
ber.open(r"C:\Users\SRINIVAS\Documents\Python Scripts"+r'\ih.html')