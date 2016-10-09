# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 21:53:03 2016

@author: SRINIVAS
"""

st="http://www.pythonchallenge.com/pc/def/map.html"
abc=list('abcdefghijklmnopqrstuvwxyzabcdefg')
listy=[]
for elem in st:
    if elem not in abc:
        listy.append(elem)
    else:
        listy.append(abc[abc.index(abc[abc.index(elem)+2])])
print(''.join(listy))

"""
from string import maketrans
intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!"
print str.translate(trantab)
"""