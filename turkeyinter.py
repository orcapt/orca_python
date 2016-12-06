#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 10:22:14 2016

@author: Pranavtadepalli
"""

#from PIL import Image, ImageTk
import tkinter
import random
import time

#images=[tkinter.PhotoImage(file="turkish.gif"),tkinter.PhotoImage(file="turkey.gif")]

a=time.time()
for elem in range(5):
    root = tkinter.Toplevel()
    root.geometry('{}x{}'.format(random.randint(500,1500), random.randint(500,1500)))
    img = tkinter.PhotoImage(file=random.choice(["turkish.gif",'turkey.gif','turker.gif','dead.gif','yum.gif','more.gif']))
    # reference PhotoImage in local variable

    button = tkinter.Button(root, image=img)

    button.grid()
    tkinter.mainloop()

b=time.time()
print('Your score is ', 20-(b-a))