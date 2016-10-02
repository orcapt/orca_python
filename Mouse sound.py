# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 13:12:15 2016

@author: SRINIVAS
"""

import winsound
import tkinter
p=tkinter.Tk()
for elem in range(10000):
    winsound.Beep(2*p.winfo_pointerxy()[0]+38,round(p.winfo_pointerxy()[1]/5))
    print(p.winfo_pointerxy())