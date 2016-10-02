# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 15:01:54 2016

@author: SRINIVAS
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'