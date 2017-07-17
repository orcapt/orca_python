#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 16:30:45 2017

@author: Pranavtadepalli
"""

from selenium import webdriver
from bs4 import BeautifulSoup as soup
import time
import pyautogui
import pyzmail
import imapclient
chromedriver = '//Users/Pranavtadepalli/Downloads/chromedriver'
browser = webdriver.Chrome(chromedriver)
browser.get('http://www.freenom.com/en/index.html?lang=en')
username = browser.find_element_by_name("domainname")
username.send_keys("xcfgh")
browser.find_element_by_id("submitBtn").click()
time.sleep(5)

for elem in browser.find_elements_by_xpath("//a[contains(text(), 'Get it now!')]"):
    try: 
        try:
            print(123234323432)
            elem.click()
            break
        except:
            browser.execute_script('document.getElementsByClassName("addSelect getItNow borderRadius")[0].scrollIntoView();')
            print(123234323432)
            elem.click()
            break
    except Exception as e: 
        print(e)
print(browser.find_elements_by_xpath("//a[contains(text(), 'Get it now!')]"))


browser.execute_script('''window.open("https://my.freenom.com/cart.php?a=confdomains&language=english","_blank");''')
browser.switch_to_window(browser.window_handles[1])
time.sleep(1)
"""
username = browser.find_element_by_name("myemail")
username.send_keys("dumpython@gmail.com")
browser.find_element_by_xpath('//input[@type="submit" and @class="mediumBtn primaryColor noFloat"]').click()

#Verify My Email Address

"""
browser.execute_script('document.getElementsByClassName("freenomBtn useForward")[0].click()')
#freenomBtn useDNS
try:
    browser.find_element_by_class_name("forward_input").clear()
    browser.find_element_by_class_name("forward_input").send_keys("https://www.google.com")
except:
    browser.find_element_by_class_name("forward_input").clear()
    browser.find_element_by_class_name("forward_input").send_keys("https://www.google.com")
browser.find_element_by_id("configure_submit_button").click()
time.sleep(2)

browser.execute_script('document.getElementsByName("myemail")[0].value="dumpython@gmail.com"')
browser.find_element_by_css_selector(".mediumBtn.primaryColor.noFloat").click()
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('dumpython@gmail.com ', '........')
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['ALL'])
rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
message = pyzmail.PyzMessage.factory(rawMessages[UIDs[-1]][b'BODY[]'])
print(message.text_part.get_payload().decode(message.text_part.charset))
time.sleep(10)
browser.quit()

