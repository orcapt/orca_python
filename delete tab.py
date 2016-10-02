# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 09:19:30 2016

@author: SRINIVAS
"""

import tkinter
from tkinter import messagebox

top=tkinter.Tk()

me=tkinter.Button(top,text='pie',command=print(0))

me.grid(column=12,row=10)
e=tkinter.Button(top,text='pie',command=print(0))
e.grid(column=5,row=10)
me.pack()
e.pack()
top.mainloop()