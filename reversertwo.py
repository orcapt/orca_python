#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 20:32:39 2017

@author: Pranavtadepalli
"""

[print(a) for a in range(10000000) if int(''.join(list(reversed(str(a)))))*2==a]