#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 19:31:13 2016

@author: Pranavtadepalli
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 18:37:12 2016

@author: Pranavtadepalli
"""

import PIL
import math
im=PIL.Image.new('RGB', (100,100))


def fun(x,y):
    try:
        x=abs((x*2)-math.sin(x)+2)
        while x>99:
            x=x-100
        y=abs((y*4)+math.sin(y)-3)
        while y>99:
            y=y-100
        print(x,y)
        t=[[int(round(x)),int(round(y))],((int(round((x*2)))),int(round(x+y)),int(round(y*2)))]
        return(t)
    except:
        print('error')
    
x=0
y=0
for e in range(100):
    for t in range(100):
        try:
            im.putpixel(fun(x,y)[0],fun(x,y)[1])
            x=fun(x,y)[1][0]

            y=fun(x,y)[1][1]
        except:
            print('error1')
im.show()