#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 17:45:38 2017

@author: Pranavtadepalli
"""


from selenium import webdriver
from bs4 import BeautifulSoup as soup
chromedriver = '//Users/Pranavtadepalli/Downloads/chromedriver'
browser = webdriver.Chrome(chromedriver)
browser.get('https://www.wolframalpha.com/input/?i='+'what is 9*9+4.4')
browser.find_element_by_name('equal').click()
source=browser.page_source
source=soup(source,'lxml')
#print(source)
try:
    stuff=source.findAll('wa-no-query-link',class_="ng-scope ng-isolate-scope")
    #print(stuff)
    for elem in stuff:
            pie=elem
    print(str(pie).split('title')[-1].split('"')[1].strip('.'))
except:
    stuff=source.findAll('a',class_="ng-scope ng-isolate-scope")
    #print(stuff)
    for elem in stuff:
            pie=elem
    print(str(pie).split('title')[-1].split('"')[1].strip('.'))
listy=[]
"""
for elem in stuff:
    try:
        print(elem.attrs['class'])
        if elem.attrs['class']==['linkno-query-link']:
            print(elem)
            #listy.append(elem)
    
    except KeyError:
        pass
        #print('real',elem)
#print(listy)
#print(listy[1].attr['alt'])
"""
