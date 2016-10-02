# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 14:06:00 2016

@author: SRINIVAS
"""

import requests

r = requests.get('https://mail.google.com/mail/u/0/#inbox')
c = r.cookies
i = c.items()

for name, value in i:
    print(name, value)