# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 11:45:26 2016

@author: SRINIVAS
"""

from bs4 import BeautifulSoup as soup
import webbrowser
from gtts import gTTS
import speech_recognition as sr
#import sys
import time
import urllib.request
tts = gTTS(text="I'm listening...", lang='en')
tts.save("hl.mp3")
webbrowser.open(r"C:\Users\SRINIVAS\Documents\Python Scripts\hl.mp3")
print("I'm listening...")

time.sleep(1)
r = sr.Recognizer()

try:
    with sr.Microphone() as source:                # use the default microphone as the audio source
                audio = r.listen(source)
                
                b=r.recognize_google(audio)
except:
    tts = gTTS(text="Say something or I'm giving up on you", lang='en')
    tts.save("hl.mp3")
    webbrowser.open(r"C:\Users\SRINIVAS\Documents\Python Scripts\hl.mp3")
    time.sleep(2)
    try:

        with sr.Microphone() as source:                # use the default microphone as the audio source
                    audio = r.listen(source)
                    
                    b=r.recognize_google(audio)
    except:
        tts = gTTS(text="I'm giving up on you", lang='en')
        tts.save("hl.mp3")
        webbrowser.open(r"C:\Users\SRINIVAS\Documents\Python Scripts\hl.mp3")
        #sys.exit(1)
        quit()

print('Question:',b)

inputs=b
inputs=inputs.split(' ')
t='https://answers.search.yahoo.com/search;_ylt=AwrXoCE45N5XRCcAYodPmolQ?p='
for elem in inputs:
    t=t+'+'+elem
t=t+'&fr2=sb-top&fr=uh3_answers_vert_gs&type=2button'
#print(t)
#raw=urllib.request.urlopen('https://answers.search.yahoo.com/search;_ylt=AwrXoCE45N5XRCcAYodPmolQ?p=hi+fun+people&fr2=sb-top&fr=uh3_answers_vert_gs&type=2button').read()
raw=urllib.request.urlopen(t).read()
raw=soup(raw)
t=raw.find_all('a',href=True)
t=str(t)
listy=[]
for elem in t.split('href='):
    if len(elem.split('https://answers.yahoo.com/question/index'))>1:
        listy.append(elem.split('"')[1])
#print(listy[0])
if len(listy)==0:
    ft='I do not know'
else:
    raw=urllib.request.urlopen(listy[0]).read()
    raw=soup(raw)
    #raw=str(raw)
    #print(soup.get_text(raw)[1:100000])
    ft=raw.find_all(class_='ya-q-full-text')[0].get_text()
print('Answer:',ft)
tts = gTTS(text=ft, lang='en')
tts.save("hl.mp3")
webbrowser.open(r"C:\Users\SRINIVAS\Documents\Python Scripts\hl.mp3")
#raw.find_all(class_='ya-q-full-text')[0].get_text())
"""
print(raw.split('Hi there, how are you? and You')[0][-1:-1000])
print('\n')
print(raw.split('Hi there, how are you? and You')[1][1:1000])
#print(raw)
"""