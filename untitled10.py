#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 21:20:25 2016

@author: Pranavtadepalli
"""

import PIL
import math
im=PIL.Image.new('RGB', (1000,1000))


def fun(x,y,nz):
    try:
        t=abs(y-x+nz-math.tan(nz)+math.hypot(x,nz)*(y/x))
        if t>1000:
            t=t-1000
        r=t
        t=[(int(round(t)),int(round(y)),int(round(x)))]
        return(t)
    except:
        print('error')
    
x=0
y=0
nz=1
for x in range(1000):
    for y in range(1000):
        try:
            im.putpixel((x,y),fun(x,y,nz)[0])
            nz=fun(x,y,nz)[0][0]-nz
        except:
            print('error1')
im.show()