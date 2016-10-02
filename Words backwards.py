# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 12:13:17 2016

@author: SRINIVAS
"""

from nltk.corpus import words
from random_words import RandomWords
rw = RandomWords()
a=0
while a<20:
    
    word = rw.random_word()
    i=list(word)
    i.reverse()
    i=''.join(i)
    if i in words.words():
        print(word)
        a=a+1
