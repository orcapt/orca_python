# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 09:25:39 2016

@author: SRINIVAS
"""
"""

import sounddevice as sd

from scipy.io import wavfile
wave = wavfile.read('ine.wav')

fs= 44100
duration=4
sd.play(wave[1],wave[0])
sd.wait()
"""
import wave
import numpy
import sounddevice as sd
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