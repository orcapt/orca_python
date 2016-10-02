# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 13:04:04 2016

@author: SRINIVAS
"""

class grid:
    lists=[]
    loop=0
    def __init__(self,list1):
        self.list1=list1
        grid.loop=grid.loop+1
        self.lists.append(self.list1)
    def show(self):
        me=''
        for a in self.lists:
            me=''
            for b in a:
                me=me+b
            print(me)
a=grid([])
grid(['1','2','3','4','5'])
grid(['5','4','3','2','1'])
a.show()
        