# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 18:34:33 2016

@author: SRINIVAS
"""
from ImageLite import ImageLite
f = open('eve.jpg','rb')
data = f.read()
img = ImageLite(data)
print(img.width, img.height, img.image_type)