# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 10:14:27 2016

@author: PRANAV
"""
from path import path
a=''
p=path(r'C:\Users\PRANAV\Documents\Python Scripts')
orca=p.files(pattern='*.py')
def replace(a):
    ie=open(a,'r')
    pie=ie.read()
    ert=pie.replace('SRINIVAS','PRANAV')
    print(ert)
    ie.close()
    ei=open(a,'w')
    ei.write(ert)
    ei.close()
for elem in orca:
    replace(elem)



