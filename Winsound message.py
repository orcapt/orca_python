# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 13:26:23 2016

@author: SRINIVAS
"""

import winsound
import matplotlib.pyplot as plt
ha=[]
with open('mec.wav', 'rb') as f:
    data = f.read()
for elem in data:
    byte = elem
    hexadecimal = hex(byte)
    decimal = int(hexadecimal, 16)
    ha.append(decimal)
plt.plot(ha)
plt.show()