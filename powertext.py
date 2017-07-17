#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 21:31:21 2017

@author: Pranavtadepalli
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
created on Fri May 26 19:07:56 2017

@author: Pranavtadepalli
"""
from selenium import webdriver
from bs4 import BeautifulSoup as soup
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    chromedriver = '//Users/Pranavtadepalli/Downloads/chromedriver'
    browser = webdriver.Chrome(chromedriver)
    browser.get('https://lgusd.powerschool.com/public/home.html')
    username = browser.find_element_by_name("account")
    password = browser.find_element_by_name("pw")
    
    username.send_keys("prantadepa")
    password.send_keys("17802249")
    
    browser.find_element_by_id("btn-enter").click()
    raw=soup(browser.page_source)
    browser.quit()
    simp='-'.join([elem.text for elem in raw.findAll('td') if elem.text!='\xa0']).split('-.-.-.-.-')
    teachers=[]
    for grade in simp[1:]:
        current=[]
        current.append(grade.split('\xa0')[0])
        current.append(' '.join(grade.split(',')[1].split('\xa0Email')))
        current.append(grade.split(':')[1].split('(')[0].split('-')[-4])
        teachers.append(current)
    resp = MessagingResponse().message(str(teachers))
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True,port=4040)