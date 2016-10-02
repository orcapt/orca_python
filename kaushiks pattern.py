# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 20:01:04 2016

@author: PRANAV
"""
a=[6]
let=input('how many numbers would you like')
lister=[0]
fi=0
me=[0]
i=-1
my=''
while fi<int(let):
    fi=fi+1
    for thing in a:
        
            
        pie=list(str(thing))
        
        for item in pie:
            
            
            if item not in me:
                it=pie.count(item)
                my=str(my)+str(it)+str(item)
                lister.append(item)
                me.append(item)
        print(a)
        a=[]
        me=[]
        
        a.append(int(my))
        my=''
        
        
            