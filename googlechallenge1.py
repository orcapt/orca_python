# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 11:45:27 2016

@author: PRANAV
"""


import re
import os
import urllib.request
import webbrowser
urls=[]
mau=[]
guad=[]
pi=open('place_code.google.com','r')

fi=pi
me=0
meyer='0'
he=''
pi=pi.read()
pi=pi.split('\n')
fi.close()
for elem in pi:
    
    if re.search('/edu/', elem, re.M|re.I):
        #print(elem)
        t=elem.split(' ')
        urls.append('http://code.google.com'+(t[6]))

for elem in urls:
    nerd=elem.split('-')
    
    berd=[nerd[-1],nerd[0]+'-'+nerd[1]+'-'+nerd[2]+'-'+nerd[3]+'-']
    guad.append(berd)
guad.sort()

for elem in guad:
    ipo=elem[1]+elem[0]
    mau.append(ipo)
    
urls=mau
#print(urls)
os.mkdir(r"C:\Users\PRANAV\Documents\Python Scripts\hi54")
os.chdir(r"C:\Users\PRANAV\Documents\Python Scripts\hi54")
for elem in urls:
    me=int(me)
    me=me+1
    me=str(me)
    he='image'+me+'.jpg'
    urllib.request.urlretrieve(elem,he)
    

file = open("index.html", "w")
file.write('<verbatim>')
file.write('<html>')
file.write('<body>')
fier=0
pile=399
while fier<pile:
    meyer=int(meyer)
    fier=fier+1
    meyer=fier+1
    meyer=str(meyer)
    file.write(r'<img src="C:\Users\PRANAV\Documents\Python Scripts\hi54\image'+meyer+'.jpg">')
file.write('</body>')
file.write('</html>')
file.close()
webbrowser.open(r'C:\Users\PRANAV\Documents\Python Scripts\hi54\index.html')
