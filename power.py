#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 21:53:02 2016

@author: Pranavtadepalli
"""
import requests
r = requests.get('https://www.mathxlforschool.com/login_school.htm', auth=('prantadepa@lgusd.org', 'Pt17802249'))


r.encoding=r.encoding
print(r.headers)
print('')
a=r.text
for elem in a.split(';'):
    print(elem)
print('')
print(r.cookies)