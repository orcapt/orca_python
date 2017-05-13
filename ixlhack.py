#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 11:34:05 2017

@author: Pranavtadepalli
"""
import requests 
payload = { 'username': 'prantadepa', 'password': '17802249' } 
payload1={'q'}
with requests.Session() as s:
	p = s.post('https://www.ixl.com/signin/losgatos', data=payload) 
	#print(p.text)
	r = s.post('https://www.ixl.com/math/kindergarten/add-with-pictures-sums-up-to-5', data=payload1) 
	print(r.text)