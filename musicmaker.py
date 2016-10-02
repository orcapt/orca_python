# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 12:38:42 2016

@author: SRINIVAS
"""
import time
from random import randint
from random import uniform
tre=input('how much time you got??')
a=open('sound.txt','r+')
m=a.read()
print(m)
a.close()
p=open('sound.txt','a')
rew=randint(0,3)
if rew==1:
    turt='\n'
else:
    turt='.'
p.write(turt)
p.close()
e=0
m=list(m)
mepp=uniform(.2,.4)
length=(m.count('.')*mepp)+m.count(' ')*.1
neat=int(tre)/length

neat=round(neat,0)

while e<neat:
    e=e+1
    for elem in m:
        if elem==' ':
            time.sleep(.1)
        else:
            print('\a')
            time.sleep(mepp)
