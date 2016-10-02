# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 19:12:28 2016

@author: PRANAV
"""

import time
a=15

may=0

def coolersound(may,a):
    while may<a:
        may=may+1
        print('\a')
        time.sleep(.1)
        print('\a')
        time.sleep(0.2)
        print('\a')
        time.sleep(0.3)
        print('\a')
        time.sleep(0.4)
        print('\a')
        time.sleep(0.5)
        print('\a')
        time.sleep(0.6)
        print('\a')
        time.sleep(0.7)
coolersound(may,a)
