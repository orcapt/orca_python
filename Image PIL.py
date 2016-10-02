# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 15:58:06 2016

@author: SRINIVAS
"""

import PIL
from random import randint
from random import choice
import math
image=PIL.Image.new('RGB',(1000,1000), color=0)
for x in range(1000):
    for y in range(1000):
        image.putpixel((x,y),(abs(x-y),(x+1)%(y+1),(y+1)%(x+1)))
#         image.putpixel((e,el),((randint(1,255)),randint(1,255),randint(1,255)))
#         image.putpixel((x,y),(choice([x,y])*randint(1,3),choice([x,y])*randint(1,3),choice([x,y])*randint(1,3)))
    
image.show()