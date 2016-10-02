# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 13:11:04 2016

@author: SRINIVAS
"""
'<bold/>'
def nest(alist):
    types=list(map(str,list(map(type,alist))))
    loop=-1
    fin=[]
    for elem in types:
        loop=loop+1
        if elem=="<class 'list'>":
            fin.append(alist[loop])
    try:
        return(fin[0])
    except IndexError:
        return(alist)
p=[':sub:',':super:','hello',[':high:','world',[':small:','hi']]]
string=''
def fun1(listy,string):
    save=''
    for elem in listy:
            try:
                if len(elem.split(':'))==3:
                    
                    string=string+'<'+elem.strip(':')+'>'
                    save=save+'<'+'/'+elem.strip(':')+'>'
                elif str(type(elem))!="<class 'list'>":
                    string=string+elem
            except AttributeError:
                string=fun(elem,string)
    return(string+save)
def fun(listy,string):
        save=''
        for elem in listy:
            try:
                if len(elem.split(':'))==3:
                    
                    string=string+'<'+elem.strip(':')+'>'
                    save=save+'<'+'/'+elem.strip(':')+'>'
                elif str(type(elem))!="<class 'list'>":
                    string=string+elem
            except AttributeError:
                string=fun1(elem,string)
        return(string+save)
save=''
for elem in p:
    
    try:
        if len(elem.split(':'))==3:
            string=string+'<'+elem.strip(':')+'>'
            save=save+'<'+'/'+elem.strip(':')+'>'
        elif str(type(elem))!="<class 'list'>":
            string=string+elem

            
    except AttributeError:
        print(elem)
        string=fun(elem,string)
print(string+save)