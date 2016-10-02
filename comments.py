# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 18:50:14 2016

@author: SRINIVAS
"""
rewe=input('filename?')
def length(name):
    crel=open(name,'r')
    return(len(crel.read().split('\n')))
    crel.close()
def read(name,line):
    pie=open(name,'r')
    fi=pie.read()
    fi=fi.split('\n')
    return(fi[int(line-1)])
    pie.close()

def write(name,line,text):
    pi=open(name,'r')
    me=pi.read()
    
    f=me.split('\n')
    f[line-1]=text
    pi.close()
    ip=open(name,'w+')
    
    for elem in f:
        ip.writelines(elem)
        ip.writelines('\n')
    ip.close()
def comment(comment,line,name):
    write(name,line,read(name,line)+'#   '+comment)


for elem in range(1,length(rewe)):
    a=read(rewe,elem)
    if list(a)[0:3]==['d','e','f']:
        orc=a.split('def')[1]
        orca=orc.split('(')[0]
        o=orca.split(' ')[1]
        comment(input('What does function '+o+' do?\n'),elem,rewe)






