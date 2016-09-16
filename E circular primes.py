# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 17:09:32 2016

@author: SRINIVAS
"""

def circle(number):
    listy=[]
    number=list(number)
    for elem in number:
        listy.append(int(''.join(number)))
        a=number[0]
        number.pop(0)
        number.append(a)
    return listy
def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True
def primes(number):
   if int(str(number)[-1])%2==0:
       return(False)
   else:
       me=range(2,round(number*.54))
       he=True
       for elem in me:
           if number%elem==0:
               
               he=False
       if number!=1 and number!=0: 
           return he
       else:
           return False

ha=[]
for ele in range(1000000):
    if isprime(ele):
        t=list(set(list(map(isprime,circle(str(ele))))))
    else:
        t=[False]
    if len(t)==1:
        if t[0]==True:
            for e in circle(str(ele)):
                ha.append(e)
print(len(list(set(ha))))

        