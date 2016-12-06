# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 17:45:21 2016

@author: SRINIVAS
"""

import sounddevice as sd
import numpy as np
import math
#import subprocess
#import os
#import wavio
import pygame
#import time
import wave
import numpy
fs= 44100
krow=[0]
duration=.1
a=0
pygame.mixer.init()
while True:
    hire=[]
    if a%1==0:
        recording = sd.rec(math.ceil(duration * fs), samplerate=fs, channels=2)
        sd.wait()
        fay=[]
        yaf=[]
        fred=math.ceil(fs*duration)-10
        for p in range(1,fred):
            fay.append(recording[p][0])
        for elem in fay:
            yaf.append(abs(elem))
    a=a+1
    
    
    krow.append(np.mean(yaf))
    for elem in krow:
        hire.append(abs(np.mean(krow)-elem))
    
    if np.mean(krow)<np.mean(yaf)-np.mean(hire):
       fp = wave.open('int.wav')
       nchan = fp.getnchannels()
       N = fp.getnframes()
       dstr = fp.readframes(N*nchan)
       data = numpy.fromstring(dstr, numpy.int16)
       data = numpy.reshape(data, (-1,nchan))
       fs= 30010
       duration=2
       sd.play(data,fs)
       sd.wait()
       print('intruder!!!')
    else:
        print('Nothing')
