# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 10:57:56 2016

@author: SRINIVAS
"""

import math
from webcolors import rgb_to_name
import tkinter
import time
import random
from PIL import ImageGrab  # Part of PIL
image = ImageGrab.grab() #Define an area to capture.

p=tkinter.Tk()
x=0

screen_width = p.winfo_screenwidth()
screen_height = p.winfo_screenheight()
lisr=[]
while x<500000:
    x=x+1
    time.sleep(0.0001)
    rgb = image.getpixel((p.winfo_pointerxy()[0], p.winfo_pointerxy()[1])) #What pixel do we want?
    lisr.append(rgb)
    #if p.winfo_pointerxy()[1]>screen_height/2:
    #    print('down')
    #else:
    #    print('up')
rgbs=set(lisr)
print('You got',len(rgbs),'colors')