# -*- coding: utf-8 -*-
"""
Created on Fri May 13 18:10:16 2016

@author: SRINIVAS
"""

import random
i=input("type a sentence to make a funny thing")
i=list(i)
consonants=['b','c','d','f','g','h','j','k','l','m','n','p','r','s','t','v','w','z']
vowels=['i','u','a','e','u','o']
f=[]
for elem in i:
    if elem=='i'or'u'or'a'or'e'or'o':
        e=''
        e=random.choice(consonants)
        f.append(e)
    if elem=='b'or'c'or'd'or'f'or'g'or'h'or'j'or'k'or'l'or'm'or'n'or'p'or"q"or'r'or's'or't'or'v'or'w'or"y"or"x"or'z':
        e=''
        e=random.choice(vowels)
        f.append(e)
    if elem==" ":
        e=''
        e=" "
        f.append(e)
print("".join(f))