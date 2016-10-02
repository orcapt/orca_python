# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 12:08:16 2016

@author: SRINIVAS
"""

import math
import tkinter
import time
import random
file=open('high.txt','a')
p=tkinter.Tk()
x=0
x1=random.randint(0,1000)
ad=1
y1=random.randint(0,700)
location=[0,1]
mer=0
me=random.randint(0,1)
em=random.randint(0,1)
def choose(x):
    if me==1:
        return(x+500)
    else:
        return(x+100)
def dist(x1,x2,y1,y2):
    dist = math.hypot(x2 - x1, y2 - y1)
    return(dist)
while x<500:
    x=x+1
    time.sleep(0.01)
    
    
    if x1<p.winfo_pointerxy()[0]<choose(x1):
        if y1<p.winfo_pointerxy()[1]<choose(y1):
            mer=mer+1
            x1=random.randint(0,1000)
            me=random.randint(0,1)
            y1=random.randint(0,700)
            
            print('+1 points')
            time.sleep(0.1)
print('Your score is ',mer)
file.write(str(mer)+'\n')
file.close()
ile=open('high.txt','r')
print('The highscore is ',max(map(int,ile.readlines())))
ile.close()