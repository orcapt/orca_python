# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 12:40:58 2016

@author: PRANAV
"""

fihi=0
mep=[]
def primes(prime):
    hi=prime
    meep=0
    kist=[]
    final=[]
    while hi!=1:
        hi=hi-1
        kist.append(hi)
    for elem in kist:
        if prime%elem==0:
            final.append(elem)
    for elem in final:
        meep=meep+elem
    return(meep)
print(primes(int(input('number'))))
pine=range(1000)
for elem in pine:
    sed=primes(elem)
    if sed==primes(sed):
        print(sed,primes(sed))
"""
while fihi<10:
    fihi=fihi+1
    mep.append(fihi)

for elem in mep:
    tree=primes(elem)
    if tree==primes(tree):
        print(tree,elem)
"""