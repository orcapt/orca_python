# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 19:12:06 2016

@author: SRINIVAS
"""
import numpy
b=numpy.eye(3)
a=0
me=0
tally1=0
tally2=0
ytally1=0
ytally2=0
x=0
b=b*0
ter=0
while ter==0:
    playxx=int(input('playerx: xcord'))
    playxy=int(input('playerx: ycord'))
    if b[playxx][playxy]==0:
        b[playxx][playxy]=1
        print(b)
    else:
        print('that spot is taken, you lost your turn')
    while a!='win':
        while x<3:
            
            if b[a][x]==1:
                tally1=tally1+1
            if b[a][x]==2:
                tally2=tally2+1
            if b[x][a]==1:
                ytally1==ytally1+1
            if b[x][a]==2:
                ytally2=ytally2+1
            x=x+1
        
        if tally1==3:
            print('player x won')
            me='win'
        if ytally1==3:
            print('player x won')
            me='win'
        
        if tally2==3:
            print('player o won')
            me='win'
        if ytally2==3:
            print('player o won')
            me='win'
        x=0
        tally1=0
        tally2=0
        ytally1=0
        ytally2=0
        a=a+1
        if me=='win':
            a=me
            ter=1
        if a==3:
            a='win'
    tally2=0
    tally1=0
    ytally1=0
    ytally2=0
    x=0
    a=0
    print('')
    print('')
    playox=int(input('playero:xcords'))
    playoy=int(input('playero:ycords'))
    if b[playox][playoy]==0:
        b[playox][playoy]=2
        print(b)
    else:
        print('that spot is taken, you lost your turn')
    
    
    while a!='win':
        while x<3:
            
            if b[a][x]==1:
                tally1=tally1+1
            if b[a][x]==2:
                tally2=tally2+1
            if b[x][a]==1:
                ytally1==ytally1+1
            if b[x][a]==2:
                ytally2=ytally2+1
            x=x+1
        
        if tally1==3:
            print('player x won')
            me='win'
        if ytally1==2:
            print('player x won')
            me='win'
        
        if tally2==3:
            print('player o won')
            me='win'
        if ytally2==3:
            print('player o won')
            me='win'
        x=0
        tally1=0
        tally2=0
        ytally1=0
        ytally2=0
        
        a=a+1
        if me=='win':
            a=me
            ter=1
        if a==3:
            a='win'
    tally2=0
    tally1=0
    ytally1=0
    ytally2=0
    x=0
    a=0
    if 0 not in b and ter==0:
        print('draw')
        ter=1
        