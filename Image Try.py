# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 11:19:54 2016

@author: SRINIVAS
"""

from PIL import Image
import numpy
im = Image.open('black1.jpg', 'r')
width, height = im.size
"""
width, height = im.size
pixel_values = list(im.getdata())
print(pixel_values[1])

data = numpy.asarray(im)
print(data[1:100][1:100])
"""
imrgb = im.convert("RGB")
f=list(imrgb.getdata())
me=[]
der=''
for w in range(height):
    for elem in me:
        der=der+elem
    print(der)
    der=''
    me=[]
    for h in range(width):
        if f[h]==(255,255,255):
            me.append('.')
        else:
            me.append(',')