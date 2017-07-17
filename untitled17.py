#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:40:30 2017

@author: Pranavtadepalli
"""

import pyautogui

for x in range(1000):
    for y in range(1000):
        pyautogui.moveTo(x, y, 0)