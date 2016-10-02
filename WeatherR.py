# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 14:39:01 2016

@author: SRINIVAS
"""
"""
import urllib

from bs4 import BeautifulSoup
url = "http://weather.weatherbug.com/MN/Wahkon-weather.html?zcode=z6286&zip=56386"
soup = BeautifulSoup(urllib.request.urlopen(url).read())
a=soup.find(name="span", id="divHi").get_text()

b=soup.find(name="span", id="divLo").get_text()
"""
from PyDictionary import PyDictionary
dictionary=PyDictionary()
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:                # use the default microphone as the audio source
    audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
try:
    a=r.recognize_google(audio)

except LookupError:                            # speech is unintelligible
    print("Could not understand audio")
s=a.split(' ')
der=-1
trte=0
if len(s)==2 and s[0]=='Define':
    srer=s[1]
    fret=dictionary.meaning(srer).items()
for elem in fret:
    print(elem[0],'\n',elem[1][0])