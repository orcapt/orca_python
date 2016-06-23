# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:50:49 2016

@author: SRINIVAS
"""
a=input('enter a sequence')
pi=[]
a=a.split(',')
for elem in a:
    pi.append(int(elem))

pie=pi
final=[]
somthing=[]
number=0
loop=0
loopy=0
loopyy=0
lenpie=0
lensomthing=0
def iteration(pi,final,somthing,number,loop,lenpie):
    final.append(pi[0])
    lenpie=len(pi)
    while loop<lenpie:
        loop=loop+1
        try:
            number=abs(pi[1]-pi[0])
            somthing.append(number)
            pi.pop(0)
        except IndexError:
            loop=1+lenpie
    loop=0
    pi.pop()

#funtion to do xxx
def oppi(pi,final,somthing,number,lensomthing,loop):
    final.append(somthing[0])
    lensomthing=len(somthing)
    while loop<lensomthing:
        loop=loop+1
        try:
            number=abs(somthing[1]-somthing[0])
            pi.append(number)
            somthing.pop(0)
        except IndexError:
            loop=1+lensomthing
    loop=0
    somthing.pop()
# end function    
    
    
while len(a)>loopy:
    loopy=loopy+1
    if loopy%2!=0:
        iteration(pi,final,somthing,number,loop,lenpie)
    else:
        oppi(pi,final,somthing,number,lensomthing,loop)
print(final)