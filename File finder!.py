# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 15:13:23 2016

@author: PRANAV
"""
from os import listdir
in1=input('What do you think you want in your file?')
files=listdir(r'C:\Users\SRINIVAS\Documents\Python Scripts')
for elem in files:
    try:
        t=open(elem,'r')
        if len(t.read().split(in1))>1:
            print(elem)
        t.close()
    except:
        pass