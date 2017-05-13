#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 18:40:32 2017

@author: Pranavtadepalli
"""


import pyqrcode
big_code = pyqrcode.create("Mickey Mouse's Behind", error='L', version=2, mode='binary')
big_code.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
big_code.show()