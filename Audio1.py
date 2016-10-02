# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 16:40:40 2016

@author: SRINIVAS
"""

import numpy
import scipy
from scipy.io.wavfile import read
from scipy.signal import hann
from scipy.fftpack import rfft
import matplotlib.pyplot as plt
snd=read('mec.wav')
audio=snd[1]
window=hann(1024)
audio=audio[0:1024]*window
mags=abs(rfft(audio))
mags=20*scipy.log10(mags)
mags -=max(mags)

plt.plot(mags)
plt.show()