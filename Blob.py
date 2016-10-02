# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 13:31:45 2016

@author: SRINIVAS
"""

from textblob import TextBlob

text = '''
I love you!
'''

blob = TextBlob(text)


for sentence in blob.sentences:
    print(sentence.sentiment.polarity)
# 0.060
# -0.341

