# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 13:23:09 2016

@author: SRINIVAS
"""

class grid:
    col1=0
    row1=0
    a=0
    type1=0
    row2=[]
    col2=[]
    def row(self,list1):
        self.list1=list1
        self.row1=self.list1
    def col(self,list1):
        self.list1=list1
        self.col1=self.list1
    """
    def axis(self,row1,col1):
         
         self.col1=col1
         self.row1=row1
         
         
        
         a=np.zeros(shape=(len(self.row1),len(self.col1)))
         self.a=a
         for p in range(len(self.col1)):
             self.a[p][0]=self.col1[p]
         for p in range(len(self.row1)):
             self.a[0][p]=self.row1[p]
    """         
    def make(self,x,y):
        import numpy as np
        a=np.zeros(shape=(x,y))
        self.a=a
    def place(self,coor,value):
        self.coor=coor
        self.value=value
        self.a[self.coor[0]+0][self.coor[1]-0]=self.value
    def show(self,type1):
        import numpy as np
        self.type1=type1
        tea=''
        
        for elem in self.row1:
            tea=tea+(' '*(len(str(self.type1))-2))+str(elem)
        
        print('  ',tea)
        print('')
        me=-1
        e=-1
        for x in np.nditer(self.a, flags=['external_loop'], order='F'):
            t=''
            me=me+1
            e=e+1
            for elem in x:
                if self.type1=='str' or self.type1=='float':
                    t=t+str(elem)+' '
                    me=me+(len(str(elem))-1)
                if self.type1=='int':
                    t=t+str(int(elem))+' '
            print(self.col1[e],' ',t)
    def get(self,coor):
        return(self.a[coor[0]+0][coor[1]-0])
def MakeTable(rows,colomns,Xlabel,Ylabel,types):
    grid1=grid()
    grid1.make(rows,colomns)
    if Xlabel=='none' and Ylabel!='none':
        grid1.col(list1=Ylabel)
    if Ylabel=='none' and Xlabel!='none':
        grid1.row(list1=Xlabel)
    if Xlabel!='none' and Ylabel!='none':
        grid1.col(list1=Ylabel)
        grid1.row(list1=Xlabel)
    grid1.show(types)
MakeTable(4,3,[1,2,3,4],[1,2,3],'float')
"""
grid1.place([0,1],5)
print(grid1.get([0,1]))
grid1.show('int')
"""

