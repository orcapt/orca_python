# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 17:59:38 2016

@author: SRINIVAS
"""

import numpy as np
from scipy.optimize import curve_fit

def func(x, a, b, c):
     return a * np.exp(b * x) + c
     
y = np.array(list(map(int,['1', '2', '8', '32', '162', '976', '6832', '54663', '491971', '4919711', '54116823', '649401885', '8442224517', '118191143240', '1772867148604', '28365874377664', '482219864420304', '8679957559565488', '164919193631744286', '3298383872634885721'])))
xdata = np.array(range(len(y)))
ydata = y
popt, pcov = curve_fit(func, xdata, ydata)
