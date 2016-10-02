# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 11:44:11 2016

@author: SRINIVAS
"""
import tkinter
import time
import random
p=tkinter.Tk()
x=0


while x<1000:
    x=x+1
    time.sleep(0.01)
    print(p.winfo_pointerxy())
    if 1315<p.winfo_pointerxy()[0]<1350:
        if 1<p.winfo_pointerxy()[1]<13:
            print("Don't Close Me!\a")
            time.sleep(0.3)
            
