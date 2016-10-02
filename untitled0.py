# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 10:14:23 2016

@author: PRANAV
"""

from path import path
import os
fwer=[]
red=[]
pot=[]
subdirectories=os.listdir(r'C:\Users\SRINIVAS\Documents\Python Scripts')

fur=os.listdir(r'C:\Users\SRINIVAS\Documents\Python Scripts')
tea=[]
wse=[]
bees=[]
lcount=-1
p=path(r'C:\Users\SRINIVAS\Documents\Python Scripts')
for orca in p.files():
    bees.append(orca.basename())

for elem in bees:
    if elem in subdirectories:
        subdirectories.remove(elem)

for ele in subdirectories:
    
    me=path(r"C:\Users\SRINIVAS\Documents\Python Scripts")
    
    hpie=os.path.join(me,ele)
    
    orcasr=os.listdir(hpie)
    #print(orcasr)
    for elm in orcasr:
        cream=str(elm)
        peem=cream+'='+hpie
        wse.append(cream)
        tea.append(peem)

#print(tea)
for elem in fur:
    meep=fur.count(elem)
    
    if meep>1:
        wert=os.path.join(me,elem)
        print(elem,' repeated',meep,' times')
        
meep=0
for eleml in wse:
    lcount=lcount+1
    meep=wse.count(eleml)
    
    if meep>1:
        
        letre=tea[lcount].split('=')
        fwer.append(letre[0]+' repeated'+str(meep)+'times and path is '+letre[1])
print(fwer)
for elem in fwer:
    if elem not in pot:
        pot.append(elem)
        rock=elem.split(' ')
        rock=rock[0]
        print(rock)
        for eem in fwer:
            if eem.split(' ')[0]==rock:
                pass
                print(eem.split(' ')[-2]+eem.split(' ')[-1])