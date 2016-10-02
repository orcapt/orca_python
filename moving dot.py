# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 12:47:06 2016

@author: PRANAV
"""

pit=0
me=''

stringspace='                            '
string=input('Make your character')
while pit!='done':
    
    
    pit=input(string+stringspace)
    pie=list(pit)
    for elem in pie:
        me=me+' '
    if '>' in pie:
        string=me+string
        stringspace=stringspace[len(pie):]
    if '<' in pie:
        string=string[len(pie):]
        stringspace=stringspace+me
    me=''
    
    