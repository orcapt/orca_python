#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 21:56:12 2017

@author: Pranavtadepalli
"""


from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time
import pyautogui
chromedriver = '//Users/Pranavtadepalli/Downloads/chromedriver'
browser = webdriver.Chrome(chromedriver)
browser.get('https://www.google.com/recaptcha/api2/demo')
x, y = pyautogui.locateCenterOnScreen('calc7key.png')