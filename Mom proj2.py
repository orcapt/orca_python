# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 19:47:04 2016

@author: SRINIVAS
"""

import csv
file=open('som.csv','r')
reader = csv.reader(file)
for row in reader:
    print(' '.join(row))