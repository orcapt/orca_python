# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 15:14:41 2016

@author: SRINIVAS
"""

from lxml import html
import requests
response = requests.get('http://www.data.gov/')
doc = html.fromstring(response.text)
link = doc.cssselect('small a')[0]
print(link.text)