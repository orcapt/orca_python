#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 19:58:32 2016

@author: Pranavtadepalli
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 20:43:22 2016

@author: Pranavtadepalli
"""



import PIL
import math
import numpy
im=PIL.Image.new('RGB', (100,100))


def fun(x,y):
    tr=[]
    loop=0
    while x<10:
        x=x**2+y
        tr.append(x)
        #tr[0]=tr[0]**2+tr[1]
        loop=loop+1
    
    
    r=numpy.mean(tr)
    b=loop
    g=numpy.mean(abs(loop-r))
    t=[(int(round(r)),int(round(b)),int(round(g)))]
    return(t)

x=0
y=0
nz=1
for x in range(100):
    print('yay')
    for y in range(100):
        try:
            im.putpixel((x,y),fun(x,y)[0])
        except:
            print('error1')
            print(fun(x,y)[0])
im.show()