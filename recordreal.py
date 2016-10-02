# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 17:41:11 2016

@author: SRINIVAS
"""

import sounddevice as sd
from scipy import linalg
import numpy
from random import randint
import time
duration = randint(2,6)  # seconds
fs=100000
me=0
recording = sd.rec(duration * fs, samplerate=fs, channels=2)
sd.wait()
sd.play(recording)
sd.wait()
me=linalg.inv(recording)
sd.play(me)
sd.wait()
"""
print(recording)
while me<10:
    me=me+1
    recording=recording*randint(1,20)
    recording[randint(0,2)][1]=randint(1,10000)
    recording[randint(0,2)][1]=randint(1,100)
    
    
    
    sd.play(recording,blocking=True)
    time.sleep(randint(0,1))
    sd.stop()
    sd.wait()
"""
    