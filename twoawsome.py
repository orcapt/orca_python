# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 17:12:09 2016

@author: SRINIVAS
"""

pi=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811]
pie=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811]
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
    
    
while len(pie)>loopy:
    loopy=loopy+1
    if loopy%2!=0:
        iteration(pi,final,somthing,number,loop,lenpie)
    else:
        oppi(pi,final,somthing,number,lensomthing,loop)
print(final)