#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 20:19:07 2016

@author: Pranavtadepalli
"""

 # -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 18:26:31 2016

@author: PRANAV
"""

from random import choice
import csv
csvfile=open('FastFactsStudy1.csv','rb')
csvfile=open('FastFactsStudy1.csv', 'r', newline='', encoding='utf8')
spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
for row in spamreader:
    print(', '.join(row))
csvfile.close()
"""
abc=list('qwertyuiopasdfghjklzxcvbnm')
fin2=[choice(abc),choice(abc),choice(abc),choice(abc),choice(abc)]
while len(set(fin2))!=5:
    fin2=[choice(abc),choice(abc),choice(abc),choice(abc),choice(abc)]
fin1=[' ',choice(listy),choice(listy),choice(listy),choice(listy),choice(listy)]
file=open('science.csv','w')
file.write(','.join(fin1))

for elem in fin2:
    file.write('\n')
    file.write(elem+',')
"""

