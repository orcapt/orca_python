# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 16:05:12 2016

@author: SRINIVAS
"""
import numpy
from pylab import*
from scipy.io import wavfile
freq,snd=wavfile.read('small.wav')
snd=snd/(2.**15)
print(snd.shape)

time=arange(0,33075,1)
time=time/freq
time=time*1000
plot(time,snd[:,0],color='k')
