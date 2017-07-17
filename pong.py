#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 12:10:06 2017

@author: Pranavtadepalli
"""
import time
import os
from pykeyboard import PyKeyboard
global gameboard
keyboard=PyKeyboard()
gameboard=[
           ['','','','','','','','','','','',''],
           ['','','','','','','','','','','',''],
           ['','','','','','','','','','','',''],
           ['','','','','','','','','','','',''],
           ['','','','','','','','','','','',''],
           ['','','','','','','','','','','',''],
           ['','','','','','','','','','','',''],
           ['|','','','','','*','','','','','','|'],
           ['','','','','','','','','','','',''],
           ['','','','','','','','','','','',''],
           ['','','','','','','','','','','',''],
           ['','','','','','','','','','','',''],
           ['','','','','','','','','','','',''],
           ['','','','','','','','','','','',''],
           ['','','','','','','','','','','',''],]
def updateboard():
    os.system('clear')
    board=''
    for elem in gameboard:
        board=board+'\n'+' '.join(elem)
    
    print(board)
    

def moveball(position):
    listnumber=-1
    for elem in gameboard:
        listindex=-1
        listnumber=listnumber+1
        for ele in elem:
            listindex=listindex+1
            if ele=='*':
                gameboard[listnumber][listindex]=''
    gameboard[position[0]][position[1]]='*'

def moveracket(direction,whichracket): #if whichracket is 0, it is the first racket, -1 is the second
    listnumber=-1
    for elem in gameboard:
        listnumber=listnumber+1
        if elem[whichracket]=='|':
            break
    if direction=='up':
        gameboard[listnumber-1][whichracket]='|'
    if direction=='down':
        gameboard[listnumber+1][whichracket]='|'
    gameboard[listnumber][whichracket]=''
def locateball():
    listnumber=-1
    for elem in gameboard:
        listnumber=listnumber+1
        listindex=-1
        for elem in elem:
            listindex=listindex+1
            if elem=='*':
                return([listnumber,listindex])
def locateracket(whichracket):
    listnumber=-1
    for elem in gameboard:
        listnumber=listnumber+1
        if elem[whichracket]=='|':
            break
    return(listnumber)

for elem in range(50):
    updateboard()
    time.sleep(0.001)
    moveball([round(elem/7),round(elem/9)])
    updateboard()
    

    
keyboard.press_keys(['Command','k'])
