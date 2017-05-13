#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 10:31:18 2017

@author: Pranavtadepalli
"""

try:
    import Image
except ImportError:
    from PIL import Image
    import pytesseract
    print(pytesseract.image_to_string(Image.open('hand.jpeg')))
   