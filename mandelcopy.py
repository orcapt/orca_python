#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 21:29:20 2016

@author: Pranavtadepalli
"""

# Mandelbrot fractal
# FB - 201003151
# Modified Andrew Lewis 2010/04/06
from PIL import Image
import math
# drawing area (xa < xb and ya < yb)
xa = -2.0
xb = 1.0
ya = -1.5
yb = 1.5
maxIt = 2056 # iterations
# image size
imgx = 1000
imgy = 1000

#create mtx for optimized access
image = Image.new("RGB", (imgx, imgy))
mtx = image.load()

#optimizations
lutx = [j * (xb-xa) / (imgx - 1) + xa for j in range(imgx)]

for y in range(imgy):
    cy = y * (yb - ya) / (imgy - 1)  + ya
    for x in range(imgx):
        c = complex(lutx[x], cy)
        z = 0
        for i in range(maxIt):
            if abs(z) > 2.0: break 
            z = z * z  +c
        r = i % 4 * 64
        g = i % 8 * 32
        b = i % 16 * 16
        mtx[x, y] =  r,g,b

image.show()