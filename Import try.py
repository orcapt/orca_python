# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 09:03:51 2016

@author: SRINIVAS
"""

from gtts import gTTS
import webbrowser
import time
import speech_recognition as sr
r = sr.Recognizer()
b='I talk other console'
while True:
    
    try:
        tts = gTTS(text=b, lang='en')
        tts.save("hl.mp3")
        webbrowser.open(r"C:\Users\SRINIVAS\Documents\Python Scripts\hl.mp3")
        with sr.Microphone() as source:                # use the default microphone as the audio source
            audio = r.listen(source)
        if b=='':
            pass
        else:
            b=r.recognize_google(audio)
    except:
        pass