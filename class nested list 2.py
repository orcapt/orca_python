# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 15:27:54 2016

@author: SRINIVAS
"""

a='sub: hi small: bye :small :sub'
listy=[]
for elem in str(a).split(" "):
    if elem[-1]==':':
        listy.append('<'+elem[0:-1]+'>')
    elif elem[0]==':':
        listy.append('</'+elem[1:]+'>')
    else:
        listy.append(elem)
print(''.join(listy))