#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 08:17:38 2017

@author: Pranavtadepalli
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import sys
row1=[2,0,0,0,0,0]
row2=[0,1,0,0,0,0]
row3=[0,0,1,0,0,0]
row4=[0,0,0,1,0,0]
row5=[0,0,0,0,1,0]
row6=[0,0,0,0,0,2]

def decide(gameboard):
    y=-1
    for elem in range(6):
        y=-1
        for el in gameboard[elem]:
                y=y+1
                side=gameboard[elem][y]
                for e in [-1,0,1]:
                    for e1 in [-1,0,1]:
                        me=0
                        try:
                            new=gameboard[e+elem][e1+y]
                            
                        except:
                            me=1
                        if me!=1 and new==side and side!=0:
                            #print(e,e1)
                            #print(elem,y)
                            hi=[]
                            try:
                                
                                if e+e1!=0:

                                    ea=0
                                    e1a=0
                                    for q in range(3):e1
                                        ea=e+ea
                                        e1a=e1+e1a
                                        new=gameboard[ea+elem][e1a+y]

                                        hi.append(new)
                            except:
                                pass
                            if len(hi)==3:
                                if hi==[side,side,side]:
                                    return side

def tie(gameboard):
    listy=[]
    for elem in range(6):
        for el in gameboard[elem]:
                listy.append(el)
    zero=[zero for zero in listy if zero==0]
    if zero==[]:
        return 1
    else:
        return 0
                                
def plot(gameboard):
    x1=[]
    y1=[]
    color=[]
    for elem in range(6):
        for el in range(6):
            x1.append(el)
    
    for ele in range(6):
        for elem in gameboard[ele]:
            if elem!=0:
                y1.append(ele)
                if elem==1:
                    color.append('yellow')
                else:
                    color.append('red')
            else:
                y1.append(-1)
                color.append('orange')
    plt.scatter(x1,y1,s=1000,color=color)
    plt.ylim([0,5])
    plt.xlim([0,5])
    plt.show({'block':False})


gameboard = np.array([row1, row2, row3, row4, row5, row6])

win=0
while win==0:
    fine=1
    print('player1 turn')
    slot=int(input('choose which slot you would like to put your piece in (0-5)'))
    while fine==1:
        fine=0
        for elem in range(6):
            if 0==gameboard[elem][slot]:
                gameboard[elem,slot]=1

                break

    plot(gameboard)
    t=decide(gameboard)
    if t==0:
        pass
    elif t==1:
        print('player1 wins')
        win=1
        sys.exit('Game Over')
    elif tie(gameboard)==1:
        print('tie')
        win=1
        sys.exit('Game Over')
    fine=1
    print('player2 turn')
    slot=int(input('choose which slot you would like to put your piece in (0-5)'))
    while fine==1:
        fine=0
        for elem in range(6):
            if 0==gameboard[elem][slot]:
                gameboard[elem,slot]=2
                break

    t=decide(gameboard)
    if t==0:
        pass
    elif t==2:
        print('player2 wins')
        win=1
        sys.exit('Game Over')
    elif tie(gameboard)==1:
        print('tie')
        win=1
        sys.exit('Game Over')
    fine=0
    plot(gameboard)
