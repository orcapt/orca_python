# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 15:47:31 2016

@author: SRINIVAS
"""

import numpy as np
import wavio
import sounddevice as sd
fs= 44100
a=0
duration=5
print(0)
recording = sd.rec(duration * fs, samplerate=fs, channels=2)
sd.wait()
print(0)

wavio.write('ine.wav',recording,rate=44100,sampwidth=3)