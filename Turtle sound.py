# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 14:36:29 2016

@author: SRINIVAS
"""

import turtle as t
from random import randint
import random
import sounddevice as sd
import numpy as np
import math
fs= 44100
krow=[0,0,0]
duration=.4

a=0
sed=[180,90,270,360]
t.speed(100000)
t.colormode(255)
while a<1000:
    t.pensize(3)
    if a%5==0:
        recording = sd.rec(math.ceil(duration * fs), samplerate=fs, channels=2)
        sd.wait()
        fay=[]
        yaf=[]
        fred=math.ceil(fs*duration)-10
        for p in range(1,fred):
            fay.append(recording[p][0])
        for elem in fay:
            yaf.append(abs(elem))
    if t.pos()[0]>100:
        t.setheading(180)
        print(0)
        t.forward(10)
    if t.pos()[0]<-100:
        t.setheading(0)
        t.forward(20)
        print(1)
        t.forward(10)
    if t.pos()[1]<-100:
        t.setheading(90)
        t.forward(10)
        print(2)
    if t.pos()[1]>100:
        t.setheading(270)
        t.forward(10)
        print(3)
    a=a+1
    t.down()
    
    print(np.mean(yaf))
    krow.append(np.mean(yaf))
    if np.mean(krow)<np.mean(yaf):
        t.pensize(10)
    else:
        t.pencolor((randint(0,255), randint(0,255), randint(0,255)))
    t.forward(randint(5,80))
    
    random.shuffle(sed)
    t.setheading(sed[0])
    random.shuffle(sed)
    
    t.setheading(sed[0])
    t.backward(randint(5,80))
    
    
