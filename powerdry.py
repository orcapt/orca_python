#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 16:26:28 2017

@author: Pranavtadepalli
"""
import dryscrape
session = dryscrape.Session()
session.visit('https://www.ixl.com/math/grade-3/multiply-by-2')
name = session.at_xpath('//*[@name="username"]') # Where <input name="username">
name.set("prantadepa@losgatos")
password = session.at_xpath('//*[@name="password"]') # Where <input name="password">
password.set("17802249")
# Push the button
name.form().submit()
session.visit("https://www.ixl.com/math/grade-3/multiply-by-2")
print(session)