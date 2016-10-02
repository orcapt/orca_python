# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 16:11:14 2016

@author: SRINIVAS
"""

from bs4 import BeautifulSoup as soup
import webbrowser
import random
import urllib.request
input1=input('Search wikipedia\n')
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url = 'https://www.google.com/search?q=green+apples'+'+'.join(input1.split(' '))
headers={'User-Agent':user_agent,} 

request=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)
data = response.read() # The data u need
raw=data
raw=soup(raw)
gsoup1=raw
#print(gsoup1)
a=gsoup1.find_all(name='img')
print(a)
urls=[]
for elem in a:
    urls.append(elem.get('src'))
real=[]
print(urls)
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
print(real)
for elem in real[1:10]:
    file.write(r'<img src="'+'https:'+elem+'">')
    file.write('\n')
file.write('</body>')
file.write('\n')
file.write('</html>')
file.write('\n')
file.close()
ber=webbrowser.get('windows-default')
ber.open(r"C:\Users\SRINIVAS\Documents\Python Scripts"+r'\ih.html')