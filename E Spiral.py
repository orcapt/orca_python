# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 20:18:32 2016

@author: SRINIVAS
"""
# add one at the end
seeds=[3,5,7,9]
add=10
final=1
for elem in range(1001):
    new=[]
    for ele in seeds:
        final=final+ele
    for eem in seeds:
        new.append(eem+add)
        add=add+2
    seeds=new
    if elem<20:
        print(seeds)
for lem in seeds:
    final=final+lem
print(final)
