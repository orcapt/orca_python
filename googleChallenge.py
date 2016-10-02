# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 15:54:06 2016

@author: PRANAV
"""
import re
import os
import urllib.request
import webbrowser
urls=[]
pi=open('animal_code.google.com','r')
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

urls.sort()
print(urls)
os.mkdir(r"C:\Users\PRANAV\Documents\Python Scripts\hi50")
os.chdir(r"C:\Users\PRANAV\Documents\Python Scripts\hi50")
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
pile=37
while fier<pile:
    meyer=int(meyer)
    fier=fier+1
    meyer=fier+1
    meyer=str(meyer)
    file.write(r'<img src="C:\Users\PRANAV\Documents\Python Scripts\hi50\image'+meyer+'.jpg">')
file.write('</body>')
file.write('</html>')
file.close()
webbrowser.open(r'C:\Users\PRANAV\Documents\Python Scripts\hi50\index.html')



