# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 18:48:32 2016

@author: SRINIVAS
"""

import matplotlib.pyplot as plt
import numpy as np
slope=0
constant=0
constant=input('What would you like your constant to be')
slope=input('What is your slope')
constant=int(constant)
slope=int(slope)
t=np.arrange(constant,0,0.001)
one=slope+constant
plt.plot([t,t*slope])

plt.show()