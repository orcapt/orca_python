#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 15:14:42 2017

@author: Pranavtadepalli
"""
import time
from flask import Flask
import subprocess
from multiprocessing import Process

def flaskapp():
    print(pi.replace('\n',''))
    app = Flask(__name__)
    @app.route('/')
    def hello_world():
        return pi
    app.run(port=5600)
def thread():
    print(subprocess.Popen('cd /Users/Pranavtadepalli/PythonStuff;./ngrok http 5600', shell=True))
if __name__ == '__main__':
  global pi
  pi=input('html please\n')
  time.sleep(3)
  p1 = Process(target=flaskapp)
  p1.start()
  p2 = Process(target=thread)
  p2.start()
  p1.join()
  p2.join()