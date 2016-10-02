# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 11:17:03 2016

@author: SRINIVAS
"""

import math
from webcolors import rgb_to_name
import tkinter
import time
import random
from PIL import ImageGrab  # Part of PIL
image = ImageGrab.grab() #Define an area to capture.
import os
clear = lambda: os.system('cls') or None
p=tkinter.Tk()
x=0
art='______________'
brt='______________'
crt='______________'
drt='______________'
ert='______________'
frt='______________'
grt='______________'
screen_width = p.winfo_screenwidth()
screen_height = p.winfo_screenheight()
lisr=[]
lists=[art,brt,crt,drt,ert,frt,grt]
while x<5000:
    clear()
    x=x+1
    print(lists[0])
    print(lists[1])
    print(lists[2])
    print(lists[3])
    print(lists[4])
    print(lists[5])
    print(lists[6])
    art='______________'
    brt='______________'
    crt='______________'
    drt='______________'
    ert='______________'
    frt='______________'
    grt='______________'
    frt='______________'
    lists=[art,brt,crt,drt,ert,frt,grt]
    time.sleep(0.01)
    f=round(p.winfo_pointerxy()[0]/100)
    o=round(p.winfo_pointerxy()[1]/100)
    lists[o]=list(lists[o])
    
    try:
        lists[o][f]='[]'
        lists[o]=''.join(lists[o])
    except IndexError:
        lists[o][f-1]='[]'
        lists[o]=''.join(lists[o])
    os.system('cls')
    clear()

