#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 20:46:35 2016

@author: Pranavtadepalli
"""

import PIL
import math
im1 = PIL.Image.open("Penguin.JPG")
im1.show()
listy=[]
factor_of_cancelation=6
c=im1.getpixel((0,0))
r=0
b=0
for a in range(im1.height):
    for b in range(im1.width):
        e=0
        d=im1.getpixel((b,a))
        loop=-1
        for elem in c:
            loop=loop+1
            if abs(d[loop]-elem)<factor_of_cancelation:
                pass
            else:
                if b!=0:
                    e=1

        if e==1:
            print(b,a)
            c=im1.getpixel((b,a))
            break
        
        else:
            c=d
            im1.putpixel((b,a),(200,200,200))
            
            
            
c=im1.getpixel((0,0))
r=0
b=0        
            
            
for a in range(im1.height):
    for b in reversed(list(range(im1.width))):
        e=0
        d=im1.getpixel((b,a))
        loop=-1
        for elem in c:
            loop=loop+1
            if abs(d[loop]-elem)<factor_of_cancelation:
                pass
            else:
                if b!=im1.width-1:
                    e=1

        if e==1:
            print(b,a)
            c=im1.getpixel((b,a))
            break
        
        else:
            c=d
            im1.putpixel((b,a),(200,200,200))
            
            


im1.save("penguin1.jpg")