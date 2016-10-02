# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 14:36:36 2016

@author: SRINIVAS
"""


import math
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd


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
"""
a=open('Z5.txt','r')
me=a.readlines()
a.close
"""
f=[]
t=[]
for elem in way:
    f.append(float(abs(elem))**2)
for elem in way:
    t.append(float(abs(elem)))
#plt.scatter(list(range(1,len(f)+1)),f,s=0.0001)
#plt.show()

area=(sum(f)*duration)/(len(f)+1)
area1=(sum(t)*duration)/(len(t)+1)
file=open('door.txt','a')
file.write('Area A^2:'+str(area)+'\n')
file.write('Area A:'+str(area1)+'\n')
file.write('Average A:'+str(np.mean(t))+'\n')
file.write('Average A^2:'+str(np.mean(f))+'\n')
file.close()