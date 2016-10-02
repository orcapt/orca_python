# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 09:41:18 2016

@author: SRINIVAS
"""

import tkinter as tk
root = tk.Tk()
for r in range(4):
    for c in range(4):
        tk.label(root, text='R%s/C%s'%(r,c),
            borderwidth=1 ).grid(row=r,column=c)
root.mainloop(  )