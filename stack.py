#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:01:25 2017

@author: Pranavtadepalli
"""

string = "In fact, a 2016 study published \
    in the journal Current Biology shows that \
    our bodies adjust to higher levels of activity, \
    resulting in a decline in weight loss, \
    even a reversal, after a few months"
listy=string.split(',') #split string by comma
newstring=[]
for segment in listy:
    if len(list(list(filter(None, segment.split(' ')))))>4: #sort out short strings
           newstring.append(segment) #add segment to the list
print(newstring)
