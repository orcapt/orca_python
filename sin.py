# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 18:26:47 2016

@author: PRANAV
"""
import time
a=int(input('num of times'))
fi=float(input('frequency'))
may=0

def coolersound(may,a):
    while may<a:
        may=may+1
        time.sleep(fi)
        print('\a')
coolersound(may,a)
