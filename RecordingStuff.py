# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 17:20:41 2016

@author: SRINIVAS
"""

import math
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import time
import random

time.sleep(2)
fay=[]
way=[]
fs= 44100
a=0
duration=4
recording = sd.rec(duration * fs, samplerate=fs, channels=2)
sd.wait()
for p in range(1,fs*duration):
    a=a+1
    if a%1==0:
        fay.append(recording[p][0])
        way.append(recording[p][1])

ase=[]
har=[]
for elem in way:
    ase.append(elem+10)
swe=max(way)
for elem in ase:
    har.append(20*(math.log10((elem/swe))))
ads=max(har)

rah=[]
for elem in har:
    ele=elem/ads  
    rah.append(ele)
har=rah
were=[]



for elem in range(len(har)):
    were.append((1.0/44100.0)*elem)
plt.plot(were,har)
plt.ylabel('A/Amax, dB')
plt.xlabel('t, seconds')
plt.show()

are=np.fft.fft(har)

are=abs(are)
print(are)

are=are/max(are)
are1=are[2:1000]


plt.plot(range(len(are1)),are1,c='green')
plt.axis([0, len(are1), min(are1), max(are1)])
plt.show()
