# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 14:51:09 2016

@author: SRINIVAS
"""

import nltk
from nltk.corpus import words
import itertools
pie=input('letters')

fi=int(input('number of letters'))
orca=list(itertools.permutations(list(pie), fi))
for elem in orca:
    
    leter=''.join(elem)
    
    
    if leter in words.words():
        print(leter)
        print('\a')
