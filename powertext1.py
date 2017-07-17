#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 19:07:56 2017

@author: Pranavtadepalli
"""
from flask import Flask, request, redirect, Response
from twilio.twiml.messaging_response import MessagingResponse
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import twilio.twiml as twiml


app = Flask(__name__)


@app.route("/")
def check_app():
    # returns a simple string stating the app is working
    return twiml.Response("It works!"), 200


@app.route("/sms", methods=["POST","GET"])
def inbound_sms():
    response = twiml.Response()
    # we get the SMS message from the request. we could also get the 
    # "To" and the "From" phone number as well
    inbound_message = request.form.get("Body")
    # we can now use the incoming message text in our Python application
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
    if inbound_message != '':
        response.message(str(teachers))
    else:
        response.message("Hi! Not quite sure what you meant, but okay.")
    # we return back the mimetype because Twilio needs an XML response
    return Response(str(response), mimetype="application/xml"), 200


if __name__ == "__main__":
    app.run(debug=True)
    
    
    



    



    