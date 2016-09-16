# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 19:33:09 2016

@author: pranav
"""


l1=[]
l2=[]
cre=[]
def pal(strin):
    strin=str(strin)
    hi=list(reversed(list(strin)))
    
    if hi==list(strin):
        return(True)
    else:
        return(False)
m=range(100,1000)
for elem in m:
    for ele in m:
        mul=elem*ele
        
        if pal(mul):
            l1.append(elem)
            l2.append(ele)
            cre.append(mul)
a=max(cre)
me=cre.index(a)
print(a)
print(l1[me],'  ', l2[me])
