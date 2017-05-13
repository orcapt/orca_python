#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 09:28:27 2016

@author: Pranavtadepalli
"""
"""
import webbrowser
webbrowser.open('/Users/Pranavtadepalli/Documents/ravi.mp3')
"""
import os
import schedule
import time
def job():
    os.system("open /Users/Pranavtadepalli/Documents/ravi.mp3")

schedule.every().day.at("6:45").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)