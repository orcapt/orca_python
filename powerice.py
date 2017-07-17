#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 14:18:37 2017

@author: Pranavtadepalli
"""
#game-status-right
#if int(ss)>=90: browser.quit()
#solution=urllib.r equest.urlopen('https://www.wolframalpha.com/input/?i='+problem.replace('×','*')).read()
#solution=soup(solution)WebDriverWait(driver, 10)
#print(solution.find_all(class_="ng-isolate-scope"))
from selenium import webdriver
import time
from bs4 import BeautifulSoup as soup
import urllib.request

chromedriver = '/Users/Pranavtadepalli/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs'
chromedriver='//Users/Pranavtadepalli/Downloads/chromedriver'
while True:
    browser = webdriver.Chrome(chromedriver)
    browser.get('http://freerice.com/user/login')
    time.sleep(3)
    username = browser.find_element_by_class_name("watermarkPluginCustomClass")
    password = browser.find_element_by_name("pass")   
    username.send_keys("whackamadoodle3000")
    time.sleep(1)
    password.send_keys("orca")  
    browser.find_element_by_id("edit_submit").click()
    for elem in range(20):
        try:
            browser.execute_script('''window.open("'''+'http://freerice.com/#/multiplication-table/17548'+'''","_blank");''')
            browser.switch_to_window(browser.window_handles[1+elem])
            time.sleep(2)
            browser.find_element_by_xpath("//*[contains(text(), '84')]").click()
            
        except: pass
    print(soup(browser.page_source).find(id_='game-status-right'))
    browser.quit()



