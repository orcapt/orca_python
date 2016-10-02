# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 09:41:18 2016

@author: SRINIVAS
"""

import tkinter as tk

mert=0
me=''
pie=2
row=0
col=0
def hi(row,col):
    me=input('Number')
    
    ort=row*col-1
    meat[ort]=meat[ort].set(me)
    tk.Button(root,
        borderwidth=1,command=lambda:hi(r,c),textvariable=meat[ort]).grid(row=row,column=col)
    tree.set(me)
root = tk.Tk()
if pie!=1:
    var=tk.StringVar()
    var1=tk.StringVar()
    var2=tk.StringVar()
    var3=tk.StringVar()
    var4=tk.StringVar()
    var5=tk.StringVar()
    var6=tk.StringVar()
    var7=tk.StringVar()
    var8=tk.StringVar()
    var9=tk.StringVar()
    var10=tk.StringVar()
    var11=tk.StringVar()
    var12=tk.StringVar()
    var13=tk.StringVar()
    var14=tk.StringVar()
    var15=tk.StringVar()
    meat=[var,var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15]
    for elem in meat:
        elem.set('0')
pie=1
for r in range(4):
    
    for c in range(4):
        tree=meat[mert]
        mert=mert+1
        tk.Button(root,
            borderwidth=1,command=lambda:hi(r,c),textvariable=tree).grid(row=r,column=c)
mert=0
root.mainloop(  )