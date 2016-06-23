# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 13:31:00 2016

@author: SRINIVAS
"""

import random
from random import randint
cows=0
bulls=0
answer=list(str(randint(1000,9999)))
guess=[]
tries=0
while guess!=answer:
    tries=tries+1
    guess=list(str(input('pick a number')))
    if guess[0]==answer[0]:
        cows=cows+1
    if guess[1]==answer[1]:
       cows=cows+1
    if guess[2]==answer[2]:
       cows=cows+1
    if guess[3]==answer[3]:
       cows=cows+1
    bulls=4-cows
    print('You have',bulls,'bulls and',cows,'cows')
    bulls=0
    cows=0
print('You won in',tries,'tries')
    
            