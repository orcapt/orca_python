# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 18:55:20 2016

@author: SRINIVAS
"""
from nltk.corpus import wordnet
in1=input('STRING\n')
def posi(listy):
    t=[]
    for elem in range(len(listy)):
        t.append(''.join(listy))
        listy.pop()

        
    return t
done=0
final=[]
while done==0:
    word=[]
    for elem in posi(list(in1)):
        if wordnet.synsets(elem):
            word.append(elem)
    theone=''
    for ele in word:
        if len(ele)>len(theone):
            theone=ele
    print(theone)
    final.append(theone)
    in1=in1[len(theone):]
    if in1=='':
        done=1
print(' '.join(final))        
"""
for elem in list(in1):
    it=it+1
    listy.append(elem)
    if it!=1:
        if ''.join(listy) in words.words() and len(''.join(listy)):
            final.append(''.join(listy))
            listy=[]
        else:
            pass
"""

#print(final)