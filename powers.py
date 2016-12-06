#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 16:32:36 2016

@author: Pranavtadepalli
"""

from bs4 import BeautifulSoup as soup
import urllib.request
import os
raw=urllib.request.urlopen('https://www.mathxlforschool.com/Student/Dashboard.aspx').read()
print(raw)
