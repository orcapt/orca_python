#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 08:52:08 2017

@author: Pranavtadepalli
"""

from nltk.corpus import wordnet as wn
from stop_words import get_stop_words
stopwords=get_stop_words('en')
sent1='how do you cook pasta'.split(' ')
sent2='what are some good recipes for cooking pasta'.split(' ')
sent1syn=[]
sent1syn=[]
for elem in sent1:
    for e in wn.synsets(elem):
        