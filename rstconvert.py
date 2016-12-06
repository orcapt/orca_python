#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 18:39:12 2016

@author: Pranavtadepalli
"""

import pypandoc

#converts markdown to reStructured
z = pypandoc.convert_file('Users/Pranavtadepalli/WordInfo/README.rst','rst',format='markdown')

#writes converted file
with open('WordInfo/README.rst','w') as outfile:
    outfile.write(z)