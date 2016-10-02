# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 20:14:39 2016

@author: SRINIVAS
"""

class grid:
    import numpy as np
    
    col1=0
    row1=0
    a=0
    type1=0
    row2=[]
    col2=[]

      
    def make(self,x,y,nest):
        
        
        a=self.np.array(nest)
        self.a=a
    def place(self,coor,value):
        self.coor=coor
        self.value=value
        self.a[self.coor[0]+0][self.coor[1]-0]=self.value
    def show(self):
        
        
        
        print('  ')
        
        me=-1
        e=-1
        listy=[]
        for x in self.np.nditer(self.a, flags=['external_loop'], order='F'):
            for elem in x:
                listy.append(len(str(elem)))
        for x in self.np.nditer(self.a, flags=['external_loop'], order='F'):
            t=''
            me=me+1
            e=e+1
            for elem in x:
                    t=t+str(elem)+(max(listy)+1-len(str(elem)))*' '
            print(t)
    def get(self,coor):
        return(self.a[coor[0]+1][coor[1]+1])
        
"""
    def nested(self,neste):
        loop2=-1
        loop1=-1
        for x in neste:
            loop2=-1
            loop1=loop1+1
            for y in x:
                loop2=loop2+1
                print(y)
                self.a[loop2][loop1]=y
        print(self.a)
"""

grid1=grid()
grid1.make(3,5,[[' ','Trial1','Trial2'],['Humidity',5,6],['Temp',1,2]])
print(grid1.get([-1,0]),grid1.get([0,0]),grid1.get([1,0]))

#grid1.nested([['temp','temp','temp'],['temp','temp','temp'],['temp','temp','temp'],['temp','temp','temp'],['temp','temp','temp']])
grid1.show()
"""
grid1.place([0,1],5)
print(grid1.get([0,1]))
grid1.show('int')
"""

