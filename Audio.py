# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 16:24:21 2016

@author: SRINIVAS
"""

import numpy
from pylab import*
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
snd=read('mec.wav')
audio=snd[1]

plt.plot(audio[0:100])
plt.show()