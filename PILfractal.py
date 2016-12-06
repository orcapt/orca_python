#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 18:37:12 2016

@author: Pranavtadepalli
"""

import PIL
import math
im=PIL.Image.new('RGB', (100,100))


def fun(x,y):
    try:
        return([[abs(round(3.141593*x-y/5-math.hypot(y-x+y*2,x-y+x))),abs(round(3.1415*y-x-y+y-x*3+y**1.1+y-x*math.sin(x)))],(y*2,x+y,y)])
    except:
        pass
    

for e in range(100):
    for t in range(100):
        try:
            im.putpixel(fun(e,t)[0],fun(e,t)[1])
        except:
            print('error')
im.show()