#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 16:22:05 2017

@author: Pranavtadepalli
"""

#if int(ss)>=90: browser.quit()
#solution=urllib.r equest.urlopen('https://www.wolframalpha.com/input/?i='+problem.replace('×','*')).read()
#solution=soup(solution)
#print(solution.find_all(class_="ng-isolate-scope"))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as soup
import urllib.request

chromedriver = '//Users/Pranavtadepalli/Downloads/chromedriver'
browser = webdriver.Chrome(chromedriver)
browser.get('https://www.ixl.com/')
username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")   
username.send_keys("prantadepa@losgatos")
password.send_keys("17802249")  
browser.find_element_by_id("qlsubmit").click()

def solveIXL(problem):        
    try:
        solution=int(problem.split(':')[1].split(' ')[0])*int(problem.split(':')[1].split(' ')[2])
    except:
        time.sleep(1)
        try:
            solution=int(problem.split(':')[1].split(' ')[0].split('*')[0])*int(problem.split(':')[1].split(' ')[0].split('*')[1])
        except:
            solution=1
    return solution
for elem in range(25):
    browser.execute_script('''window.open("https://www.ixl.com/math/grade-3/multiply-by-6","_blank");''')
    browser.switch_to_window(browser.window_handles[1+elem])
    source=soup(browser.page_source,'lxml')
    time.sleep(1)
    ss=source.findAll("span", {"id": "currentscore"})[0].get_text()
    ss=int(ss)
    print(ss)
    if ss>=90: browser.quit()
    if 1==1:
        problem = None
        while problem is None:
            try:
                source=soup(browser.page_source,'lxml')
                problem=source.find_all(class_="math")[0].get_text().replace('×','*').replace('\xa0','')
            except:
                browser.execute_script('''location.reload();''')
            
    solution=solveIXL(problem)
    answer=browser.find_element_by_class_name("fillIn")
    answer.send_keys(solution)
    time.sleep(1)
    try:
        browser.find_elements_by_xpath("//button[contains(text(), 'Submit')]")[1].click()
    except:
        browser.find_elements_by_xpath("//button[contains(text(), 'Submit')]")[0].click()
    time.sleep(0.5)

    