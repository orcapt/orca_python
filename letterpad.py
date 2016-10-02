# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 20:42:38 2016

@author: SRINIVAS
"""
import nltk
from nltk.corpus import words
import itertools
pie=input('letters')
fi=len(list(pie))

orca=list(itertools.permutations(list(pie), fi))
for elem in orca:
    
    leter=''.join(elem)
    
    
    if leter in words.words():
        print(leter)

