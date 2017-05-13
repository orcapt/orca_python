#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 16:35:24 2017

@author: Pranavtadepalli
"""

import requests
from lxml import html
from lxml import etree
payload = {
	"account": "prantadepa", 
	"ps": "17802249", 
	"pstoken": "2487740952blikJnOcPF4E7lW6QzBcOKm07iLOcrKt"
}
session_requests = requests.session()
login_url = "https://lgusd.powerschool.com/guardian/home.html"
result = session_requests.get(login_url)

tree = html.fromstring(result.text)
#authenticity_token = list(set(tree.xpath("//input[@name='pstoken']/@value")))[0]
result = session_requests.post(
	login_url, 
	data = payload, 
	headers = dict(referer=login_url)
)
url = 'https://lgusd.powerschool.com/guardian/home.html'
result = session_requests.get(
	url, 
	headers = dict(referer = url)
)
print(result.ok)
print(result.content)
tree = html.fromstring(result.content)
print(tree.get_element_by_id("gaIframe"))