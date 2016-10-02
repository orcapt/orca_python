# -*- coding: utf-8 -*-


import numpy as np
import sounddevice as sd

fs= 44100
duration=4
recording = sd.rec(duration * fs, samplerate=fs, channels=2)
sd.wait()
fay=[]
way=[]
for p in range(1,fs*duration):
    fay.append(recording[p][0])
    way.append(recording[p][1])

me=open('Y9.txt','a')
for elem in fay:
    me.write(str(elem))
    me.write('\n')
    
me.close()

em=open('Z9.txt','a')
for elem in way:
    em.write(str(elem))
    em.write('\n')
em.close()
