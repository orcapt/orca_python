# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 19:04:54 2016

@author: SRINIVAS
"""

from gtts import gTTS
import os
import webbrowser
import speech_recognition as sr
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("hl.mp3")
    webbrowser.open(r"C:\Users\SRINIVAS\Documents\Python Scripts\hl.mp3")
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:                # use the default microphone as the audio source
                audio = r.listen(source)
                return(r.recognize_google(audio))
a=listen()
print('English:'+a)
a=a.split(' ')
b=[]
vowels=list('aeiouAEIOU')
for elem in a:
    joined=[]
    for ele in list(reversed(list(elem))):
        joined.append(ele)
        if ele in vowels:
            joined.append('va')
    joined=''.join(joined)
    joined=list(reversed(list(joined)))
    joined=''.join(joined)
    b.append(joined)
speak(' '.join(b))
print('Avanglavish:'+' '.join(b))
        