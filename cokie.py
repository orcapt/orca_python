# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 14:06:00 2016

@author: PRANAV
"""

import requests

r = requests.get('http://www.pythonchallenge.com/pc/def/0.html')
c = r.cookies
i = c.items()
print(r.url)

for name, value in i:
    print(name, value)

r = requests.post('http://rjfisher.lgusd.org/apps/pages/index.jsp?uREC_ID=383264&type=u&pREC_ID=521186', data = {'type':'i'})
r = requests.get("http://rjfisher.lgusd.org/apps/pages/index.jsp?uREC_ID=383264&type=u&pREC_ID=521186", params={'type':'i'})
print(r.url)